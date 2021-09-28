from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from core.models import Appointment, Project
from projects.serializers import AppointmentSerializer, ProjectSerializer

PROJECT_LISTS_URL = reverse('project:project-list')
APPOINTMENT_LISTS_URL = reverse('project:appointment-list')


def create_sample_project(client, **params):
    default = {
        'name': 'Cool Project',
        'type': 'Mobile App',
    }
    default.update(params)
    return Project.objects.create(client=client, **default)


class PublicProjectApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        res = self.client.get(PROJECT_LISTS_URL)
        self.assertEqual(res.status_code, 401)


class PrivateProjectApiTests(TestCase):
    fixtures = ['users', 'projects']

    def setUp(self):
        self.client = APIClient()
        staff = get_user_model().objects.all().filter(is_staff=True).first()
        self.client.force_authenticate(staff)

    def test_staff_retrieve_projects(self):
        res = self.client.get(PROJECT_LISTS_URL)
        projects = Project.objects.all().order_by('id')
        serializer = ProjectSerializer(projects, many=True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, serializer.data)

    def test_project_detail_view(self):
        project = Project.objects.first()
        url = reverse('project:project-detail', args=[project.id])
        res = self.client.get(url)
        serializer = ProjectSerializer(project)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, serializer.data)

    def test_staff_create_project(self):
        client_id = get_user_model().objects.all().filter(is_staff=False).first().id
        payload = {
            'client': client_id,
            'name': 'Froth App',
            'type': 'MA',
            'description': 'A cool app.',
            'start_date': '2021-09-19',
            'end_date': '2099-09-19',
        }
        res = self.client.post(PROJECT_LISTS_URL, payload, format='json')
        project = Project.objects.last()
        serializer = ProjectSerializer(project)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(res.data, serializer.data)

    def test_client_retrieve_project(self):
        """
        Test that client can view projects belong to him/her only
        """
        client = get_user_model().objects.all().filter(is_staff=False).first()
        self.client.force_authenticate(client)
        projects = Project.objects.all().filter(client=client)
        res = self.client.get(PROJECT_LISTS_URL)
        serializer = ProjectSerializer(projects, many=True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data), projects.count())
        self.assertEqual(res.data, serializer.data)

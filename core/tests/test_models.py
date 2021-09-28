from django.test import TestCase
from django.contrib.auth import get_user_model
from phonenumbers.phonenumberutil import NumberParseException
from core.models import Project, Appointment, Milestone, Expense
from datetime import datetime, date


class UserModelTests(TestCase):

    def setUp(self):
        self.password = 'testpass123'
        self.email = 'sample@email.com'
        self.phone = '+61426522198'

    def test_create_user(self):
        user = get_user_model().objects.create_user(
            email=self.email,
            password=self.password
        )
        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))

    def test_create_user_without_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, password=self.password)

    def test_user_email_normalized(self):
        email_before_normalized = 'sample@EMAIL.com'
        user = get_user_model().objects.create_user(
            email=email_before_normalized,
            password=self.password
        )
        self.assertEqual(user.email, self.email)

    def test_create_user_with_phone(self):
        user = get_user_model().objects.create_user(
            email=self.email,
            password=self.password,
            phone=self.phone
        )
        self.assertEqual(user.phone, self.phone)

    def test_create_user_with_invalid_phone(self):
        with self.assertRaises(NumberParseException):
            get_user_model().objects.create_user(
                email=self.email,
                password=self.password,
                phone='abcdefg'
            )

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            email=self.email,
            password=self.password
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)


class ProjectModelTests(TestCase):
    fixtures = ['users', 'projects']

    def test_project_str(self):
        project = Project.objects.first()
        self.assertEqual(str(project), f'{project.name}: {project.client.username}')


class AppointmentModelTests(TestCase):
    fixtures = ['users', 'projects', 'appointments']

    def test_appointment_str(self):
        appointment = Appointment.objects.first()
        self.assertEqual(str(appointment), f'Appointment with {appointment.client.username}')

    def test_appointment_end_time(self):
        # start_time: 09:30:00, duration: 30 minutes
        appointment1 = Appointment.objects.first()
        # start_time: 14:30:00, duration: 1 hour
        appointment2 = Appointment.objects.last()
        self.assertEqual(appointment1.end_time.strftime("%H:%M:%S"), '10:00:00')
        self.assertEqual(appointment2.end_time.strftime("%H:%M:%S"), '15:30:00')


class MilestoneModelTests(TestCase):
    fixtures = ['users', 'projects', 'appointments', 'milestones']

    def test_milestone_str(self):
        milestone = Milestone.objects.first()
        self.assertEqual(str(milestone), f'{milestone.name}: {milestone.project.name}')


class ExpenseModelTests(TestCase):
    fixtures = ['users', 'projects', 'appointments', 'milestones', 'expenses']

    def test_expense_str(self):
        expense = Expense.objects.first()
        self.assertEqual(str(expense), f'{expense.name}: {expense.amount}')

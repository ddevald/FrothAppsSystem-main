from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import Appointment, Project, Milestone, Expense
from projects.serializers import ProjectSerializer, AppointmentSerializer, MilestoneSerializer, ExpenseSerializer


class BaseViewSet(ModelViewSet):
    queryset = None
    serializer_class = None
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user_id = self.request.query_params.get('userId')
        queryset = self.queryset
        if user_id:
            user_id = int(user_id)
            queryset = queryset.filter(client__id=user_id)
        if not self.request.user.is_staff:
            queryset = queryset.filter(client=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save()


class ProjectViewSet(BaseViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class AppointmentViewSet(BaseViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class MilestoneViewSet(BaseViewSet):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializer


class ExpenseViewSet(BaseViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

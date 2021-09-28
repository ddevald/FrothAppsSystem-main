from rest_framework import serializers
from core.models import Project, Appointment, Milestone, Expense


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'client', 'name', 'type',
                  'description', 'start_date', 'due_date',
                  'uploaded_files', 'created_at')
        read_only_fields = ('id', 'created_at',)


class AppointmentSerializer(ProjectSerializer):

    class Meta:
        model = Appointment
        fields = ('id', 'project', 'client', 'employee', 'date',
                  'location', 'start_time', 'duration',
                  'notes', 'created_at')
        read_only_fields = ('id', 'created_at',)


class MilestoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Milestone
        fields = ('id', 'project', 'amount', 'name',
                  'is_finished', 'resources_url', 'due_date', 'created_at')
        read_only_fields = ('id', 'created_at',)


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Expense
        fields = ('id', 'project', 'amount', 'name',
                  'is_paid', 'due_date', 'created_at')
        read_only_fields = ('id', 'created_at',)

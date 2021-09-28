from django.conf import settings
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, \
    PermissionsMixin, \
    UserManager as BaseUserManager
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField
import datetime
import phonenumbers
import os
import uuid


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


def user_avatar_file_path(instance, filename):
    extension = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{extension}'
    return os.path.join('uploads/avatar', filename)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, phone=None, **extra_fields):
        if not email:
            raise ValueError('Email address must be provided.')
        email = self.normalize_email(email)
        if phone:
            phone = phonenumbers.parse(phone, None)
        user = self.model(email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email=email,
            password=password,
            is_superuser=True,
            is_staff=True
        )
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom user model
    """
    email = models.EmailField(
        max_length=255, unique=True, blank=False, null=False)
    username = models.CharField(max_length=50, blank=False, null=False)
    avatar = models.ImageField(blank=True, upload_to=user_avatar_file_path)
    # projects = models.ManyToManyField('Project')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(max_length=200, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def active_projects_counts(self):
        return self.projects.filter(is_active=True).count()

    def past_projects_counts(self):
        return self.projects.filter(is_active=False).count()


class Project(models.Model):
    """
    Project model
    """
    # PROJECT_TYPE_CHOICES = (
    #     ('MA', 'Mobile App'),
    #     ('W', 'Website'),
    #     ('WA', 'Web App'),
    #     ('SEO', 'Search Engine Optimisation'),
    #     ('DM', 'Digital Marketing'),
    #     ('UI', 'Graphic/UI Design'),
    #     ('O', 'Other')
    # )
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='projects',
        on_delete=models.SET(get_sentinel_user),
        limit_choices_to={'is_staff': False},
    )
    name = models.CharField(max_length=200)
    type = models.ManyToManyField('ProjectType')
    is_active = models.BooleanField(default=True)
    uploaded_files = models.FileField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(default=datetime.date.today)
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def progress(self):
        finished = self.milestones.filter(is_finished=True).count()
        progress = finished / self.milestones.count()
        return f'{round(progress*100)}%'

    def __str__(self):
        return f'{self.name}: {self.client.username}'


class Appointment(models.Model):
    """
    Appointment model
    """
    DURATION_CHOICES = (
        ('00:30:00', '30 minutes'),
        ('01:00:00', '1 hour'),
        ('01:30:00', '1.5 hour'),
        ('02:00:00', '2 hour'),
    )
    project = models.ForeignKey(
        'Project',
        related_name='appointments',
        on_delete=models.CASCADE,
    )
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='client_appointments',
        on_delete=models.CASCADE,
        limit_choices_to={'is_staff': False},
    )
    employee = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='employee_appointments',
        limit_choices_to={'is_staff': True},
    )
    date = models.DateField(default=datetime.date.today)
    location = models.CharField(max_length=2000)
    start_time = models.TimeField()
    duration = models.DurationField(choices=DURATION_CHOICES, default='00:30:00')
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def end_time(self):
        start_date_time = datetime.datetime.combine(datetime.date.today(), self.start_time)
        end_time = (start_date_time + self.duration).time()
        return end_time

    def __str__(self):
        return f'Appointment with {self.client.username}'


class Milestone(models.Model):
    """
    Milestone model
    """
    project = models.ForeignKey(
        'Project',
        related_name='milestones',
        on_delete=models.CASCADE,
    )
    amount = MoneyField(max_digits=13, decimal_places=2, default_currency='AUD')
    name = models.TextField(max_length=200)
    is_finished = models.BooleanField(default=False)
    resources_url = models.URLField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}: {self.project.name}'


class Expense(models.Model):
    """
    Expense model
    """
    project = models.ForeignKey(
        'Project',
        related_name='invoice',
        on_delete=models.CASCADE
    )
    amount = MoneyField(max_digits=13, decimal_places=2, default_currency='AUD')
    name = models.CharField(max_length=200)
    is_paid = models.BooleanField(default=False)
    due_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}: {self.amount}'


class ProjectType(models.Model):
    name = models.CharField(max_length=200, unique=True)
    icon = models.ImageField(blank=True, upload_to='projectType/icon')

    def __str__(self):
        return self.name

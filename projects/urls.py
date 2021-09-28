from django.urls import path, include
from rest_framework.routers import DefaultRouter
from projects import views


app_name = 'project'

router = DefaultRouter()
router.register('projects', views.ProjectViewSet)
router.register('appointment', views.AppointmentViewSet)
router.register('milestone', views.MilestoneViewSet)
router.register('expense', views.ExpenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

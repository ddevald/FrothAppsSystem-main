from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


app_name = 'user'

router = DefaultRouter()
router.register('clients', views.ClientUserViewSet)
router.register('staff', views.StaffUserViewSet)

urlpatterns = [
    path('create/', views.CreateUserAPIView.as_view(), name='create'),
    path('auth/', views.CreateTokenView.as_view(), name='auth'),
    path('me/', views.ManageUserAPIView.as_view(), name='me'),
    path('', include(router.urls)),
]

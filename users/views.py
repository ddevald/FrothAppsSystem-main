from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model

from .serializers import UserSerializer, AuthTokenSerializer


class CreateUserAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user



class BasicViewSet(ModelViewSet):
    queryset = None
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)

    def get_queryset(self):
        user_id = self.request.query_params.get('userId')
        queryset = self.queryset
        if user_id:
            user_id = int(user_id)
            queryset = queryset.filter(id=user_id)
        return queryset


class ClientUserViewSet(BasicViewSet):
    queryset = get_user_model().objects.filter(is_staff=False)


class StaffUserViewSet(BasicViewSet):
    queryset = get_user_model().objects.filter(is_staff=True)

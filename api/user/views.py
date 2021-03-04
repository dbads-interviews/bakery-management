# from rest_framework import generics, mixins, viewsets
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth import logout, get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
# from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from . import serializers
from .utils import get_and_authenticate_user, create_user_account

User = get_user_model()


class UsersViewset(viewsets.ModelViewSet):
  serializer_class = serializers.UserSerializer
  queryset = User.objects.all()
  permission_classes = [IsAdminUser]

  @action(methods=['GET'], detail=False)
  def profile(self, request):
    user = get_object_or_404(User, id=request.user.id)
    serialized_user = self.serializer_class(user)
    return Response(serialized_user.data, status=status.HTTP_200_OK)


class AuthViewSet(viewsets.GenericViewSet):
  permission_classes = [AllowAny, ]
  serializer_class = serializers.EmptySerializer
  serializer_classes = {
      'login': serializers.UserLoginSerializer,
      'register': serializers.UserRegisterSerializer,
  }
  queryset = ''

  @action(methods=['POST', ], detail=False)
  def login(self, request):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_and_authenticate_user(**serializer.validated_data)
    data = serializers.AuthUserSerializer(user).data
    return Response(data=data, status=status.HTTP_200_OK)

  @action(methods=['POST', ], detail=False)
  def register(self, request):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = create_user_account(**serializer.validated_data)
    data = serializers.AuthUserSerializer(user).data
    return Response(data=data, status=status.HTTP_201_CREATED)

  @action(methods=['POST', ], detail=False)
  def logout(self, request):
    # Token.objects.get(user=request.user).delete()
    logout(request)
    data = {'success': 'Sucessfully logged out'}
    return Response(data=data, status=status.HTTP_200_OK)

  @action(methods=['POST'], detail=False, permission_classes=[IsAuthenticated, ])
  def password_change(self, request):
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    request.user.set_password(serializer.validated_data['new_password'])
    request.user.save()
    return Response(status=status.HTTP_204_NO_CONTENT)

  def get_serializer_class(self):
    if not isinstance(self.serializer_classes, dict):
      raise ImproperlyConfigured("serializer_classes should be a dict mapping.")

    if self.action in self.serializer_classes.keys():
      return self.serializer_classes[self.action]
    return super().get_serializer_class()

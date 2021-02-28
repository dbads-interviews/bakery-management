from django.contrib.auth.models import User
# from rest_framework import generics, mixins, viewsets
from rest_framework import viewsets
from .serializers import UserSerializer


class UsersViewset(viewsets.ModelViewSet):
  serializer_class = UserSerializer
  queryset = User.objects.all()

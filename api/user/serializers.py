from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(
      style={'input_type': 'password'},
      min_length=6,
      max_length=68,
      write_only=True)

  class Meta:
    model = User
    fields = ['username', 'password', 'id', 'is_superuser']

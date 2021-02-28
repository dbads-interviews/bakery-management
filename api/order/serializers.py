from .models import Order
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields = ['user', 'total', 'items', 'id']

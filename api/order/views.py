from .models import Order
# from rest_framework import generics, mixins, viewsets
from rest_framework import viewsets
from .serializers import OrderSerializer


class OrderViewset(viewsets.ModelViewSet):
  serializer_class = OrderSerializer
  queryset = Order.objects.all()

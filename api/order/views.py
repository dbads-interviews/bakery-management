from .models import Order
# from rest_framework import generics, mixins, viewsets
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import OrderSerializer


class OrderViewset(viewsets.ModelViewSet):
  serializer_class = OrderSerializer
  queryset = Order.objects.all()

  permission_classes = [IsAuthenticated]

  def list(self, request):
    if not request.user.is_staff:
      orders = Order.objects.filter(user__id=request.user.id)
      orders = self.serializer_class(orders, many=True)
      return Response(orders.data)
    return super().list(self, request)

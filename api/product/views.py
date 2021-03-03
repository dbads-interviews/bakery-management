from .models import Product
# from rest_framework import generics, mixins, viewsets
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import ProductSerializer


class ProductViewset(viewsets.ModelViewSet):
  serializer_class = ProductSerializer
  queryset = Product.objects.all()
  permission_classes = [IsAuthenticated, IsAdminUser, ]

  def list(self, request):
    print(self.request.user, self.request.user.is_staff)
    return super().list(self, request)

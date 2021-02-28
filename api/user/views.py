from django.contrib.auth.models import User
# from rest_framework import generics, mixins, viewsets
from rest_framework import viewsets
from .serializers import UserSerializer


# class UserListGenericAPIView(
#         generics.GenericAPIView,
#         mixins.CreateModelMixin, mixins.ListModelMixin):
#   serializer_class = UserSerializer
#   queryset = User.objects.all()
#   lookup_field = 'id'

#   def get(self, request):
#     return self.list(request)

#   def post(self, request):
#     return self.create(request)


# class UserDetailGenericAPIView(
#         generics.GenericAPIView,
#         mixins.DestroyModelMixin, mixins.RetrieveModelMixin,
#         mixins.UpdateModelMixin):
#   serializer_class = UserSerializer
#   queryset = User.objects.all()
#   lookup_field = 'id'

#   def get(self, request, id=None):
#     return self.retrieve(request)

#   def put(self, request, id=None):
#     return self.update(request, id)

#   def delete(self, request, id=None):
#     return self.destroy(request, id)


class UsersViewset(viewsets.ModelViewSet):
  serializer_class = UserSerializer
  queryset = User.objects.all()

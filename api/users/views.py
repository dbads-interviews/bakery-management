from django.contrib.auth.models import User
from rest_framework import generics, mixins
from .serializers import UserSerializer
# Create your views here.

# def create_user(request):
#   # create user


class UserGenericAPIView(generics.GenericAPIView,
                         mixins.CreateModelMixin, mixins.ListModelMixin,
                         mixins.DestroyModelMixin, mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin):
  serializer_class = UserSerializer
  queryset = User.objects.all()
  lookup_field = 'id'

  def get(self, request, id=None):
    if id:
      return self.retrieve(request)
    else:
      return self.list(request)

  def post(self, request):
    return self.create(request)

  def put(self, request, id=None):
    return self.update(request, id)

  def delete(self, request):
    return self.destroy(request, id)

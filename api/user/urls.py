from django.urls import path, include
# from .views import UserListGenericAPIView, UserDetailGenericAPIView, UsersViewset
from .views import UsersViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', UsersViewset, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]

from django.urls import path, include
# from .views import UserListGenericAPIView, UserDetailGenericAPIView, UsersViewset
from .views import AuthViewSet, UsersViewset
from rest_framework.routers import DefaultRouter

auth_router = DefaultRouter()
auth_router.register('', AuthViewSet, basename='users_auth')

user_router = DefaultRouter()
user_router.register('', UsersViewset, basename='users')

urlpatterns = [
    path('', include(user_router.urls)),
    path('auth/', include(auth_router.urls)),
]

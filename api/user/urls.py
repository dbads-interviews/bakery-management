from django.urls import path, include
# from .views import UserListGenericAPIView, UserDetailGenericAPIView, UsersViewset
from .views import UsersViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', UsersViewset, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    # path('/', UserListGenericAPIView.as_view(), name='user_list'),
    # path('/<int:id>', UserDetailGenericAPIView.as_view(), name='user_detail'),
]

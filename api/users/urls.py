from django.urls import path
from .views import UserGenericAPIView

urlpatterns = [
    path('/', UserGenericAPIView.as_view(), name='users'),
    path('/<int:id>', UserGenericAPIView.as_view(), name='user_detail')
]

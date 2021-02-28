from django.urls import path, include
from .views import ProductViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', ProductViewset, basename='products')

urlpatterns = [
    path('', include(router.urls)),
]

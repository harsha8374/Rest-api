from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonalDetailViewSet

router = DefaultRouter()
router.register(r'personaldetails', PersonalDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

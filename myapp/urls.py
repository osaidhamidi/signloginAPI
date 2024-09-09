from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginViewSet, SignupViewSet

router = DefaultRouter()
router.register(r'login', LoginViewSet, basename='login')
#router.register(r'signup', SignupViewSet, basename='signup')


urlpatterns = [
    path('', include(router.urls)),
]


from django.urls import path
from .views import UserAuthenticate

urlpatterns = [
    path('auth/login/', UserAuthenticate.as_view(), name='login-endpoint'),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='signup'),
]
from django.shortcuts import render
from django.views.generic.edit import FormView

from rest_framework.viewset import ViewSet

from .models import User


class UserViewSet(ViewSet):
    """
    ViewSet from user
    """
    model_class = User
    #serializer_class = UserSerializer

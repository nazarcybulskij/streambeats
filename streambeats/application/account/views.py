from django.shortcuts import render
from django.views.generic.edit import FormView

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import User

from .serializers import UserSerializer

class UserViewSet(ModelViewSet):
    """
    ViewSet from user
    """
    #model = User
    model_class = User
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
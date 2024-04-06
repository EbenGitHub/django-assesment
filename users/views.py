from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer

# Create your views here.
class UserList(generics.ListCreateAPIView):
    """
    List all users or create a new user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
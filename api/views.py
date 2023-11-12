from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status

from cocktails.models import MixedDrinks
from .serializer import CocktailSerializer, UserSerializer


# Create your views here.
class CocktailList(generics.ListAPIView):
    queryset = MixedDrinks.objects.all()
    serializer_class = CocktailSerializer

class CocktailCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = MixedDrinks.objects.all()
    serializer_class = CocktailSerializer

class UserList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer



class CocktailDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = MixedDrinks.objects.all()
    serializer_class = CocktailSerializer
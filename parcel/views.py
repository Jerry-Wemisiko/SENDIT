from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .models import CustomUser, Order, Location
from .serializers import UserSerializer, OrderSerializer, LocationSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer


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

# class OrderDetail(viewsets.ModelViewSet):
    

class LocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

=======
from django.contrib.auth import login, logout
from django.contrib.auth.models import update_last_login
from rest_framework import viewsets, generics, status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from .models import CustomUser, Order, Location
from .serializers import UserSerializer, OrderSerializer, LocationSerializer, NewUserSerializer, LoginUserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = NewUserSerializer
    permission_classes = (AllowAny,)


class UserLoginAPIView(APIView):
    queryset = CustomUser.objects.all()
    serializer_class = LoginUserSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = LoginUserSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        update_last_login(None, user)
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        print(request.user)
        return Response({"status": status.HTTP_200_OK, "Token": token.key})


@api_view()
@permission_classes((permissions.AllowAny,))
def logout_view(request):
    logout(request)
    return Response({"status": status.HTTP_200_OK, "logged_out": "success"})


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all().order_by('date_joined')
    serializer_class = UserSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('created_at')
    serializer_class = OrderSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


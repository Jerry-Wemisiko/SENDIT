from rest_framework import serializers
from parcel.models import CustomUser, Order, Location


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['url', "first_name", "last_name", "phonenumber","username", 'email', "address", "orders"]


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
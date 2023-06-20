from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
class UserSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'password', 'company_name']



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'


class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Device
        fields='__all__'
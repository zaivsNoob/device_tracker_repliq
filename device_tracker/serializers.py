from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'password', 'company_name']



from django.urls import path, include

from rest_framework import routers, serializers, viewsets
from .models import Registration
# Serializers define the API representation.


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

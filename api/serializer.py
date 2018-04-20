from rest_framework import serializers
from .models import Request, Ambulance

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('latitude','longitude','description', 'number','timestamp')

class AmbulanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ambulance
        fields = ('latitude','longitude','status')
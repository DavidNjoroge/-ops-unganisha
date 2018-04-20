from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from rest_framework.views import APIView
from .serializer import RequestSerializer, AmbulanceSerializer
from rest_framework import status

# Create your views here.
class RequestList(APIView):
    def get(self, request, format=None):
        all_merch = Request.objects.all()
        serializers = RequestSerializer(all_merch, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = RequestSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class AmbulanceList(APIView):
    def get(self, request, format=None):
        all_merch = Ambulance.objects.all()
        serializers = AmbulanceSerializer(all_merch, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = AmbulanceSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

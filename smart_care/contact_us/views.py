from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
# Create your views here.

class ContactUs_ViewSet(viewsets.ModelViewSet):
    queryset = models.Contact_Us.objects.all()
    serializer_class = serializers.ContactUsSerializer
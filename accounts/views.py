from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework import viewsets, permissions
from .models import Address
from .serializers import AddressSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
     pass

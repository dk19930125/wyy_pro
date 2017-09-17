from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets
from rest_framework.views import APIView

from .models import SKU
from .serializers import SKUSerializer

class SKUViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SKU.objects.all().order_by('-id')

    serializer_class = SKUSerializer
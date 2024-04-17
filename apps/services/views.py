from rest_framework import generics

from .models import ServicePage, Service
from .serializers import ServicePageSerializer, ServiceSerializer


class ServicePageAPIView(generics.ListAPIView):
    queryset = ServicePage.objects.all()
    serializer_class = ServicePageSerializer


class ServiceAPIView(generics.RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'id'


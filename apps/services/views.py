from rest_framework import generics

from .models import ServicePage
from .serializers import ServicePageSerializer


class ServicePageAPIView(generics.ListAPIView):
    queryset = ServicePage.objects.all()
    serializer_class = ServicePageSerializer

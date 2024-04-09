from rest_framework import generics

from .models import AboutPage
from .serializers import AboutPageSerializer


class AboutPageAPIView(generics.ListAPIView):
    queryset = AboutPage.objects.all()
    serializer_class = AboutPageSerializer

from rest_framework import generics

from .models import AboutPage, Video
from .serializers import AboutPageSerializer, VideoSerializer


class AboutPageAPIView(generics.ListAPIView):
    queryset = AboutPage.objects.all()
    serializer_class = AboutPageSerializer


class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

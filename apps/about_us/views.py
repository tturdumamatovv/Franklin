from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AboutPage, Video
from .serializers import AboutPageSerializer, VideoSerializer


class AboutPageAPIView(generics.ListAPIView):
    queryset = AboutPage.objects.all()
    serializer_class = AboutPageSerializer


class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoHome(APIView):
    def get(self, request):
        video = Video.objects.filter(preload=False).first()
        serializer = VideoSerializer(video)
        return Response(serializer.data)


class VideoPreload(APIView):
    def get(self, request):
        video = Video.objects.filter(preload=True).first()
        serializer = VideoSerializer(video)
        return Response(serializer.data)

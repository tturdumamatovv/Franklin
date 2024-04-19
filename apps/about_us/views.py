from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import AboutPage, Video, Image, SiteInfo
from .serializers import AboutPageSerializer, VideoSerializer, SiteInfoSerializer


class AboutPageAPIView(generics.ListAPIView):
    queryset = AboutPage.objects.all()
    serializer_class = AboutPageSerializer


class VideoListView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


class VideoHome(APIView):
    def get(self, request):
        video = Video.objects.filter(preload=False).first()
        serializer = VideoSerializer(video, context={'request': request})
        return Response(serializer.data)


class VideoPreload(APIView):
    def get(self, request):
        video = Video.objects.filter(preload=True).first()
        serializer = VideoSerializer(video, context={'request': request})
        return Response(serializer.data)


class SiteInfoAPIView(APIView):
    def get(self, request):
        info_list = SiteInfo.objects.all()
        info = info_list[0]
        is_admin = request.user.is_staff

        serializer = SiteInfoSerializer(info, context={'is_admin': is_admin})

        return Response(serializer.data)
from rest_framework.views import APIView

from .serializers import AllPagesSerializer, PreloadSerializer
from apps.contacts.models import Preload

from rest_framework.response import Response


class AllPagesView(APIView):
    def get(self, request):
        serializer = AllPagesSerializer(instance={}, context={'request': request})
        return Response(serializer.data)


class PreloadView(APIView):
    def get(self, request):
        preload_instance = Preload.objects.get()
        serializer = PreloadSerializer(preload_instance, context={'request': request})
        return Response(serializer.data)


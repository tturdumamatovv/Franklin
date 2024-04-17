from rest_framework.views import APIView

from .serializers import AllPagesSerializer, PreloadSerializer

from rest_framework.response import Response


class AllPagesView(APIView):
    def get(self, request):
        serializer = AllPagesSerializer({})
        return Response(serializer.data)


class PreloadView(APIView):
    def get(self, request):
        serializer = PreloadSerializer({})
        return Response(serializer.data)


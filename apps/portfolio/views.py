from rest_framework import generics, status
from rest_framework.response import Response

from .models import (
    PortfolioPage,
    PortfolioProject,
    PortfolioDuration
)

from .serializers import (
    MainPagePortfolioSerializer,
    PortfolioProjectSerializer,
    PortfolioDurationSerializer,
    PortfolioProjectListSerializer,
    PortfolioDurationWithProjectsSerializer
)


class PortfolioPageListView(generics.ListAPIView):
    queryset = PortfolioPage.objects.all()
    serializer_class = MainPagePortfolioSerializer


class PortfolioProjectDetailView(generics.RetrieveAPIView):
    queryset = PortfolioProject.objects.all()
    serializer_class = PortfolioProjectSerializer
    lookup_field = 'id'


class PortfolioDurationListView(generics.ListAPIView):
    queryset = PortfolioDuration.objects.all()
    serializer_class = PortfolioDurationSerializer


class PortfolioProjectListView(generics.ListAPIView):
    queryset = PortfolioProject.objects.all()
    serializer_class = PortfolioProjectListSerializer


class PortfolioDurationWithProjectsDetailView(generics.RetrieveAPIView):
    queryset = PortfolioDuration.objects.all()
    serializer_class = PortfolioDurationWithProjectsSerializer
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
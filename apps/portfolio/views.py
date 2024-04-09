from rest_framework import generics

from .models import (
    PortfolioPage,
    PortfolioProject,
    PortfolioDuration
)

from .serializers import (
    MainPagePortfolioSerializer,
    PortfolioProjectSerializer,
    PortfolioDurationSerializer,
    PortfolioProjectListSerializer
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

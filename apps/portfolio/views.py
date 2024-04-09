from rest_framework import generics

from .models import (
    PortfolioPage,
    PortfolioProject,
    PortfolioDuration
)

from .serializers import (
    MainPagePortfolioSerializer,
    PortfolioProjectSerializer,
    PortfolioDurationSerializer
)


class PortfolioPageListView(generics.ListAPIView):
    queryset = PortfolioPage.objects.all()
    serializer_class = MainPagePortfolioSerializer


class PortfolioProjectListView(generics.ListAPIView):
    queryset = PortfolioProject.objects.all()
    serializer_class = PortfolioProjectSerializer


class PortfolioDurationListView(generics.ListAPIView):
    queryset = PortfolioDuration.objects.all()
    serializer_class = PortfolioDurationSerializer

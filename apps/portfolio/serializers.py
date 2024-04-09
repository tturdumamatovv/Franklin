from rest_framework import serializers

from .models import (
    PortfolioPage,
    PortfolioProject,
    PortfolioImage,
    PortfolioDuration
)


class MainPagePortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioPage
        fields = ('title', 'content')


class PortfolioDurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioDuration
        fields = ('name', 'image')


class PortfolioImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioImage
        fields = ('image', )


class PortfolioProjectSerializer(serializers.ModelSerializer):
    image = PortfolioImageSerializer()

    class Meta:
        model = PortfolioProject
        fields = ('title', 'description', 'location', 'image')

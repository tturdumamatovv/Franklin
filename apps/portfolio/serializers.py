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
        fields = ('title', 'sub_title')


class PortfolioDurationSerializer(serializers.ModelSerializer):
    page = MainPagePortfolioSerializer()

    class Meta:
        model = PortfolioDuration
        fields = ('slug', 'page', 'name', 'name_en', 'name_ru', 'image',)


class PortfolioImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PortfolioImage
        fields = ('image',)


class PortfolioDurationForProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioDuration
        fields = ('name', 'name_en', 'name_ru', 'slug')


class PortfolioProjectSerializer(serializers.ModelSerializer):
    images = PortfolioImageSerializer(many=True, read_only=True)
    duration = PortfolioDurationForProjectSerializer()

    class Meta:
        model = PortfolioProject
        fields = ('title', 'title_en', 'title_ru', 'description', 'description_en', 'description_ru',
                  'location', 'location_en', 'location_ru', 'images', 'duration')


class PortfolioProjectListSerializer(serializers.ModelSerializer):
    images = PortfolioImageSerializer(many=True, read_only=True)
    duration = PortfolioDurationForProjectSerializer()

    class Meta:
        model = PortfolioProject
        fields = ('slug', 'images', 'duration')


class PortfolioProjectToRetrieveSerializer(serializers.ModelSerializer):
    images = PortfolioImageSerializer(many=True, read_only=True)

    class Meta:
        model = PortfolioProject
        fields = ('title', 'title_en', 'title_ru', 'description',  'description_en',  'description_ru',
                  'location', 'location_en', 'location_ru', 'images', 'slug')


class PortfolioDurationWithProjectsSerializer(serializers.ModelSerializer):
    projects = PortfolioProjectToRetrieveSerializer(many=True, read_only=True)

    class Meta:
        model = PortfolioDuration
        fields = ('id', 'name', 'name_en', 'name_ru', 'image', 'projects')

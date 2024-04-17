from rest_framework import serializers

from apps.contacts.models import Preload
from apps.portfolio.models import PortfolioPage
from apps.services.models import ServicePage
from apps.contacts.models import Contact
from apps.about_us.models import AboutPage


class AboutPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPage
        fields = '__all__'


class ContactPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class PortfolioPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioPage
        fields = '__all__'


class ServicePageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicePage
        fields = '__all__'


class AllPagesSerializer(serializers.Serializer):
    about_page = serializers.SerializerMethodField()
    portfolio_page = serializers.SerializerMethodField()
    service_page = serializers.SerializerMethodField()
    contact_page = serializers.SerializerMethodField()

    def get_about_page(self, obj):
        instance = AboutPage.objects.first()
        return AboutPageSerializer(instance).data if instance else None

    def get_portfolio_page(self, obj):
        instance = PortfolioPage.objects.first()
        return PortfolioPageSerializer(instance).data if instance else None

    def get_service_page(self, obj):
        instance = ServicePage.objects.first()
        return ServicePageSerializer(instance).data if instance else None

    def get_contact_page(self, obj):
        instance = Contact.objects.first()
        return ContactPageSerializer(instance).data if instance else None


class PreloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preload
        fields = '__all__'

from rest_framework import serializers

from apps.contacts.models import Preload
from apps.portfolio.models import PortfolioPage, PortfolioDuration
from apps.services.models import ServicePage
from apps.contacts.models import Contact
from apps.about_us.models import AboutPage

from apps.about_us.serializers import AboutPageSerializer
from apps.contacts.serializers import ContactSerializer
from apps.portfolio.serializers import MainPagePortfolioSerializer
from apps.services.serializers import ServicePageSerializer


class AllPagesSerializer(serializers.Serializer):
    about_page = serializers.SerializerMethodField()
    portfolio_page = serializers.SerializerMethodField()
    service_page = serializers.SerializerMethodField()
    contact_page = serializers.SerializerMethodField()

    def get_about_page(self, obj):
        instance = AboutPage.objects.first()
        return AboutPageSerializer(instance, context=self.context).data if instance else None

    def get_portfolio_page(self, obj):
        instance = PortfolioPage.objects.first()
        return MainPagePortfolioSerializer(instance, context=self.context).data if instance else None

    def get_service_page(self, obj):
        instance = ServicePage.objects.first()
        return ServicePageSerializer(instance, context=self.context).data if instance else None

    def get_contact_page(self, obj):
        instance = Contact.objects.first()
        return ContactSerializer(instance, context=self.context).data if instance else None


class PreloadSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()

    class Meta:
        model = Preload
        fields = '__all__'

    def get_logo(self, obj):
        return self.context['request'].build_absolute_uri(obj.logo.url)

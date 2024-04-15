from apps.about_us.models import AboutPage
from apps.contacts.models import Contact
from apps.portfolio.models import PortfolioPage
from apps.services.models import ServicePage

from .serializers import AllPagesSerializer

from rest_framework import generics
from rest_framework.response import Response


class AllPagesView(generics.ListAPIView):
    serializer_class = AllPagesSerializer

    def get_queryset(self):
        about_page = AboutPage.load()
        contact = Contact.load()
        portfolio_page = PortfolioPage.load()
        service_page = ServicePage.load()

        return [about_page, contact, portfolio_page, service_page]

from apps.about_us.models import AboutPage
from apps.contacts.models import Contact
from apps.portfolio.models import PortfolioPage
from apps.services.models import ServicePage

from .serializers import AllPagesSerializer

from rest_framework import generics
from rest_framework.response import Response


class AllPagesView(generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        about_page = AboutPage.load()
        contact = Contact.load()
        portfolio_page = PortfolioPage.load()
        service_page = ServicePage.load()

        serializer = AllPagesSerializer({
            'about_page': about_page,
            'contact': contact,
            'portfolio_page': portfolio_page,
            'service_page': service_page
        })

        return Response(serializer.data)

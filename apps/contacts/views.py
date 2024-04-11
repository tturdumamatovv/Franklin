from rest_framework import generics

from .models import (
    Contact,
    Application
)
from .serializers import (
    ContactSerializer,
    ApplicationSerializer
)


class ContactListView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ApplicationCreateView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

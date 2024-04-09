from django.urls import path
from .views import ServicePageAPIView

urlpatterns = [
    path('servicepage/', ServicePageAPIView.as_view(), name='servicepage'),
]

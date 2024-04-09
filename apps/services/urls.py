from django.urls import path
from .views import ServicePageAPIView

urlpatterns = [
    path('service-page/', ServicePageAPIView.as_view(), name='service-page'),
]

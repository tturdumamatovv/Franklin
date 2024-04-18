from django.urls import path
from .views import ServicePageAPIView, ServiceAPIView

urlpatterns = [
    path('service-page/', ServicePageAPIView.as_view(), name='service-page'),
    path('service/<str:slug>/', ServiceAPIView.as_view(), name='service'),
]

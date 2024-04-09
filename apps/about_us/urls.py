from django.urls import path
from .views import AboutPageAPIView

urlpatterns = [
    path('aboutpage/', AboutPageAPIView.as_view(), name='aboutpage'),
]

from django.urls import path

from .views import AboutPageAPIView

urlpatterns = [
    path('about-page/', AboutPageAPIView.as_view(), name='about-page'),
]

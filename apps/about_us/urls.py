from django.urls import path

from .views import AboutPageAPIView, VideoListView

urlpatterns = [
    path('about-page/', AboutPageAPIView.as_view(), name='about-page'),
    path('video/', VideoListView.as_view(), name='video-list'),
]

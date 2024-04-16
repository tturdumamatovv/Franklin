from django.urls import path

from .views import AboutPageAPIView, VideoHome, VideoPreload

urlpatterns = [
    path('about-page/', AboutPageAPIView.as_view(), name='about-page'),
    path('video/home/', VideoHome.as_view(), name='video_home'),
    path('video/preload/', VideoPreload.as_view(), name='video_preload'),
]


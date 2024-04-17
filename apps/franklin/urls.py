from django.urls import path
from .views import AllPagesView, PreloadView

urlpatterns = [
    path('preload/', PreloadView.as_view(), name='preload'),
    path('pages/', AllPagesView.as_view(), name='all-pages'),
]

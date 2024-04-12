from django.urls import path
from .views import AllPagesView


urlpatterns = [
    path('pages/', AllPagesView.as_view(), name='all-pages'),
]

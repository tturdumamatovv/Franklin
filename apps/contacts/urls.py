from django.urls import path

from . import views


urlpatterns = [
    path('contacts/', views.ContactListView.as_view(), name='contact-list'),
    path('applications/', views.ApplicationCreateView.as_view(), name='application-create'),
]

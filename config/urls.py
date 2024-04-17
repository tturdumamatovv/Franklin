"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from config import settings

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Franklin API",
      default_version='v1',
      description='''
      About Page API: Manages content for the About Page.
      Video APIs: Handles video content for the website.
      Contact APIs: Provides contact details and handles application submissions.
      Portfolio APIs: Manages portfolio pages, projects, and durations. 
      Service Page API: Manages content for the Service Page.
      ''',
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourapi.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/v1/', include('apps.portfolio.urls')),
    path('api/v1/', include('apps.about_us.urls')),
    path('api/v1/', include('apps.services.urls')),
    path('api/v1/', include('apps.contacts.urls')),
    path('api/v1/', include('apps.franklin.urls')),

    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
]

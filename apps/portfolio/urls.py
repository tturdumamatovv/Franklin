from django.urls import path
from . import views

urlpatterns = [
    path('portfolio-page/', views.PortfolioPageListView.as_view(), name='portfolio-page-list'),
    path('portfolio-project/', views.PortfolioProjectListView.as_view(), name='portfolio-project-list'),
    path('portfolio-duration/', views.PortfolioDurationListView.as_view(), name='portfolio-duration-list'),
]

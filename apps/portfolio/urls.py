from django.urls import path
from . import views

urlpatterns = [
    path('portfolio-page/', views.PortfolioPageListView.as_view(), name='portfolio-page-list'),
    path('portfolio-projects/', views.PortfolioProjectListView.as_view(), name='portfolio-projects'),
    path('portfolio-project/<str:slug>/', views.PortfolioProjectDetailView.as_view(), name='portfolio-project-detail'),
    path('portfolio-duration/', views.PortfolioDurationListView.as_view(), name='portfolio-duration-list'),
    path('portfolio-duration/<str:slug>/', views.PortfolioDurationWithProjectsDetailView.as_view(),
         name='portfolio-duration-detail'),
]

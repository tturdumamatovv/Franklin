from django.urls import path
from . import views

urlpatterns = [
    path('portfolio-page/', views.PortfolioPageListView.as_view(), name='portfolio-page-list'),
    path('portfolio-projects/', views.PortfolioProjectListView.as_view(), name='portfolio-projects'),
    path('portfolio-project/<int:id>/', views.PortfolioProjectDetailView.as_view(), name='portfolio-project-detail'),
    path('portfolio-duration/', views.PortfolioDurationListView.as_view(), name='portfolio-duration-list'),
    path('portfolio-duration/<int:id>/', views.PortfolioDurationWithProjectsDetailView.as_view(),
         name='portfolio-duration-detail'),
]

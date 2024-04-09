from django.contrib import admin

from apps.portfolio.models import PortfolioPage, PortfolioDuration, PortfolioProject, PortfolioImage


admin.site.register(PortfolioPage)
admin.site.register(PortfolioDuration)
admin.site.register(PortfolioProject)
admin.site.register(PortfolioImage)

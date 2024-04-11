import nested_admin

from django.contrib import admin

from .models import (
    PortfolioPage,
    PortfolioDuration,
    PortfolioProject,
    PortfolioImage
)


class PortfolioImageInline(nested_admin.NestedStackedInline):
    model = PortfolioImage
    extra = 1


class PortfolioProjectInline(nested_admin.NestedStackedInline):
    model = PortfolioProject
    inlines = [PortfolioImageInline, ]
    extra = 1


class PortfolioDurationInline(nested_admin.NestedStackedInline):
    model = PortfolioDuration
    inlines = [PortfolioProjectInline, ]
    extra = 1


@admin.register(PortfolioPage)
class PortfolioPageAdmin(nested_admin.NestedModelAdmin):
    inlines = [PortfolioDurationInline, ]

    class Media:
        css = {
            "all": ("css/admin.css",)
        }
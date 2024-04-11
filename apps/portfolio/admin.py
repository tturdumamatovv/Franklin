from django.contrib import admin
import nested_admin
from .models import PortfolioPage, PortfolioDuration, PortfolioProject, PortfolioImage


class BaseAdmin(nested_admin.NestedModelAdmin, admin.ModelAdmin):
    class Media:
        css = {
            "all": ("css/admin.css",)
        }


class NestedBaseInline(nested_admin.NestedStackedInline):
    extra = 0


class PortfolioImageInline(NestedBaseInline):
    model = PortfolioImage


class PortfolioProjectInline(NestedBaseInline):
    model = PortfolioProject
    inlines = [PortfolioImageInline, ]


class PortfolioDurationInline(NestedBaseInline):
    model = PortfolioDuration
    inlines = [PortfolioProjectInline, ]


@admin.register(PortfolioPage)
class PortfolioPageAdmin(BaseAdmin):
    inlines = [PortfolioDurationInline, ]


@admin.register(PortfolioDuration)
class PortfolioDurationAdmin(BaseAdmin):
    inlines = [PortfolioProjectInline, ]


@admin.register(PortfolioProject)
class PortfolioProjectAdmin(BaseAdmin):
    inlines = [PortfolioImageInline, ]

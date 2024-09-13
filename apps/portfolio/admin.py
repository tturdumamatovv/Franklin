from django.contrib import admin
import nested_admin
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableAdminMixin
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
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src = {obj.image.url} width = "300"')

    get_image.short_description = "Изображение"


class PortfolioProjectInline(NestedBaseInline):
    model = PortfolioProject
    inlines = [PortfolioImageInline, ]


class PortfolioDurationInline(NestedBaseInline):
    model = PortfolioDuration
    inlines = [PortfolioProjectInline, ]


@admin.register(PortfolioPage)
class PortfolioPageAdmin(BaseAdmin):
    # inlines = [PortfolioDurationInline, ]
    pass


@admin.register(PortfolioDuration)
class PortfolioDurationAdmin(BaseAdmin):
    # inlines = [PortfolioProjectInline, ]
    pass


@admin.register(PortfolioProject)
class PortfolioProjectAdmin(SortableAdminMixin, BaseAdmin):
    list_filter = ("duration",)
    inlines = [PortfolioImageInline, ]

@admin.register(PortfolioImage)
class PortfolioImageAdmin(SortableAdminMixin, BaseAdmin):
    list_filter = ("project",)

import nested_admin
from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin, messages
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.utils.safestring import mark_safe

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

    def save_model(self, request, obj, form, change):
        try:
            # Оборачиваем сохранение в транзакцию для обработки исключений уникальности
            with transaction.atomic():
                super().save_model(request, obj, form, change)
        except IntegrityError as e:
            # В случае ошибок уникальности, выводим сообщение об ошибке в интерфейсе администратора
            messages.error(request,
                           "Ошибка сохранения: Нарушение уникального ограничения. Пожалуйста, проверьте данные.")
        except ValidationError as e:
            # Обработка ошибок валидации модели
            messages.error(request, f"Ошибка валидации: {e}")
        except Exception as e:
            # Ловим любые другие исключения, чтобы обеспечить стабильность админки
            messages.error(request, f"Произошла неизвестная ошибка: {e}")


@admin.register(PortfolioImage)
class PortfolioImageAdmin(SortableAdminMixin, BaseAdmin):
    list_filter = ("project",)

from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class ServiceFilter(admin.SimpleListFilter):
    title = _('Сервис')
    parameter_name = 'Сервис'

    def lookups(self, request, model_admin):
        services = set([cb.service for cb in model_admin.model.objects.exclude(service__isnull=True)])
        return [(service.id, service.title) for service in services]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(service__id=self.value())
        return queryset

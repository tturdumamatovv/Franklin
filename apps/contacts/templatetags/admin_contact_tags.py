from django import template

from apps.contacts.models import Application

register = template.Library()

@register.simple_tag
def get_latest_applications(limit=10):
    return Application.objects.order_by('-id')[:limit]

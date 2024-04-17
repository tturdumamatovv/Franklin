from django.contrib import admin

from .models import (
    Address,
    Contact,
    SocialLink,
    Phone,
    Email,
    Application, Preload
)


class AddressInline(admin.TabularInline):
    model = Address
    extra = 0


class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 0


class EmailInline(admin.TabularInline):
    model = Email
    extra = 0


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 0


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [
        AddressInline,
        PhoneInline,
        EmailInline,
        SocialLinkInline,
    ]


admin.site.register(Application)
admin.site.register(Preload)

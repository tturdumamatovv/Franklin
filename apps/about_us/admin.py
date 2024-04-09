from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.contrib.admin import StackedInline
from polymorphic.admin import (
    PolymorphicInlineSupportMixin,
    StackedPolymorphicInline,
    PolymorphicParentModelAdmin,
    PolymorphicChildModelAdmin
)
from .models import AboutPage, ContentBlock, ImagesBlock, SliderBlock, Image, Slide


class ImageInline(StackedInline):
    model = Image


class SlideInline(StackedInline):
    model = Slide


class ImagesBlockAdmin(PolymorphicChildModelAdmin):
    inlines = [ImageInline, ]


class SliderBlockAdmin(PolymorphicChildModelAdmin):
    inlines = [SlideInline, ]


class ImageBlockInline(StackedPolymorphicInline.Child):
    model = ImagesBlock


class SliderBlockInline(StackedPolymorphicInline.Child):
    model = SliderBlock


class ContentBlockInline(StackedPolymorphicInline):
    model = ContentBlock
    child_inlines = (
        ImageBlockInline,
        SliderBlockInline,
    )


class AboutPageAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    inlines = [ContentBlockInline, ]


admin.site.register(AboutPage, AboutPageAdmin)


class ContentBlockChildAdmin(PolymorphicChildModelAdmin):
    base_model = ContentBlock


class ContentBlockAdmin(PolymorphicParentModelAdmin):
    base_model = ContentBlock
    child_models = (ImagesBlock, SliderBlock)


admin.site.register(ContentBlock, ContentBlockAdmin)
admin.site.register(ImagesBlock, ImagesBlockAdmin)
admin.site.register(SliderBlock, SliderBlockAdmin)
# admin.site.register(ImagesBlock, ContentBlockChildAdmin)
# admin.site.register(SliderBlock, ContentBlockChildAdmin)

from django.contrib import admin
from django.contrib.admin import StackedInline
from polymorphic.admin import (
    PolymorphicInlineSupportMixin,
    StackedPolymorphicInline,
    PolymorphicParentModelAdmin,
    PolymorphicChildModelAdmin
)

from .models import (ServicePage, ContentBlock, ServiceImage, SliderBlock, Service, Slide, Icon, IconsBlock,
                     AboutServiceImage, AboutService, Step, StepBlock)


class ImageInline(StackedInline):
    model = ServiceImage


class SlideInline(StackedInline):
    model = Slide


class IconsInline(StackedInline):
    model = Icon


class ImagesBlockAdmin(PolymorphicChildModelAdmin):
    inlines = [ImageInline, ]


class SliderBlockAdmin(PolymorphicChildModelAdmin):
    inlines = [SlideInline, ]


class IconsBlockAdmin(PolymorphicChildModelAdmin):
    inlines = [IconsInline, ]


class AboutBlockInline(StackedPolymorphicInline.Child):
    model = AboutService


class SliderBlockInline(StackedPolymorphicInline.Child):
    model = SliderBlock


class IconsBlockInline(StackedPolymorphicInline.Child):
    model = IconsBlock


class ContentBlockInline(StackedPolymorphicInline):
    model = ContentBlock
    child_inlines = (
        AboutBlockInline,
        SliderBlockInline,
        IconsBlockInline,
    )


class AboutPageAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    inlines = [ContentBlockInline, ]


class ContentBlockAdmin(PolymorphicParentModelAdmin):
    base_model = ContentBlock
    child_models = (ImagesBlock, SliderBlock, IconsBlock)


admin.site.register(AboutPage, AboutPageAdmin)
admin.site.register(ContentBlock, ContentBlockAdmin)
admin.site.register(ImagesBlock, ImagesBlockAdmin)
admin.site.register(SliderBlock, SliderBlockAdmin)
admin.site.register(IconsBlock, IconsBlockAdmin)

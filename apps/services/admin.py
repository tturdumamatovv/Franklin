from django.contrib import admin
from django.contrib.admin import StackedInline

from polymorphic.admin import (
    PolymorphicInlineSupportMixin,
    StackedPolymorphicInline,
    PolymorphicParentModelAdmin,
    PolymorphicChildModelAdmin
)

from .models import (
    ServicePage,
    ContentBlock,
    IconsBlock,
    SliderBlock,
    StepBlock,
    AboutService,
    Icon,
    Slide,
    Step,
    AboutServiceImage,
    Image,
    ImagesBlock,
    Diagram
)


class ImageInline(StackedInline):
    model = Image


class SlideInline(StackedInline):
    model = Slide


class IconsInline(StackedInline):
    model = Icon


class AboutServiceImageInline(StackedInline):
    model = AboutServiceImage


class StepInline(StackedInline):
    model = Step


class ImagesBlockAdmin(PolymorphicChildModelAdmin):
    inlines = [ImageInline, ]


class SliderBlockAdmin(PolymorphicChildModelAdmin):
    inlines = [SlideInline, ]


class IconsBlockAdmin(PolymorphicChildModelAdmin):
    inlines = [IconsInline, ]


class DiagramBlockAdmin(PolymorphicChildModelAdmin):
    pass


class AboutServiceAdmin(PolymorphicChildModelAdmin):
    inlines = [AboutServiceImageInline, ]


class StepBlockAdmin(PolymorphicChildModelAdmin):
    inlines = [StepInline, ]


class ImageBlockInline(StackedPolymorphicInline.Child):
    model = ImagesBlock


class SliderBlockInline(StackedPolymorphicInline.Child):
    model = SliderBlock


class IconsBlockInline(StackedPolymorphicInline.Child):
    model = IconsBlock


class AboutServiceInline(StackedPolymorphicInline.Child):
    model = AboutService


class StepBlockInline(StackedPolymorphicInline.Child):
    model = StepBlock


class DiagramBlockInline(StackedPolymorphicInline.Child):
    model = Diagram


class ContentBlockInline(StackedPolymorphicInline):
    model = ContentBlock
    child_inlines = (
        ImageBlockInline,
        SliderBlockInline,
        IconsBlockInline,
        AboutServiceInline,
        StepBlockInline,
        DiagramBlockInline
    )


class ServicePageAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    inlines = [ContentBlockInline, ]
    class Media:
        css = {
            "all": ("css/admin.css",)
        }



class ContentBlockAdmin(PolymorphicParentModelAdmin):
    base_model = ContentBlock
    child_models = (ImagesBlock, SliderBlock, IconsBlock, AboutService, StepBlock, Diagram)


admin.site.register(ServicePage, ServicePageAdmin)
admin.site.register(ContentBlock, ContentBlockAdmin)
admin.site.register(ImagesBlock, ImagesBlockAdmin)
admin.site.register(SliderBlock, SliderBlockAdmin)
admin.site.register(IconsBlock, IconsBlockAdmin)
admin.site.register(AboutService, AboutServiceAdmin)
admin.site.register(StepBlock, StepBlockAdmin)
admin.site.register(Diagram, DiagramBlockAdmin)

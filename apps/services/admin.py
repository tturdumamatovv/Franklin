from django.contrib import admin
from django.contrib.admin import StackedInline
from django.utils.safestring import mark_safe

from polymorphic.admin import (
    PolymorphicInlineSupportMixin,
    StackedPolymorphicInline,
    PolymorphicParentModelAdmin,
    PolymorphicChildModelAdmin
)

from .filters import ServiceFilter
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
    Diagram, Service
)


class ImageInline(StackedInline):
    model = Image
    readonly_fields = ("get_image",)
    extra = 0
    def get_image(self, obj):
        return mark_safe(f'<img src = {obj.image.url} width = "300"')

    get_image.short_description = "Изображение"


class SlideInline(StackedInline):
    model = Slide
    readonly_fields = ("get_image",)
    extra = 0
    def get_image(self, obj):
        return mark_safe(f'<img src = {obj.image.url} width = "300"')

    get_image.short_description = "Изображение"


class IconsInline(StackedInline):
    model = Icon
    readonly_fields = ("get_image",)
    extra = 0
    def get_image(self, obj):
        return mark_safe(f'<img src = {obj.image.url} width = "300"')

    get_image.short_description = "Изображение"


class AboutServiceImageInline(StackedInline):
    model = AboutServiceImage
    readonly_fields = ("get_image",)
    extra = 0
    def get_image(self, obj):
        return mark_safe(f'<img src = {obj.image.url} width = "300"')

    get_image.short_description = "Изображение"


class StepInline(StackedInline):
    model = Step
    readonly_fields = ("get_image",)
    extra = 0
    def get_image(self, obj):
        return mark_safe(f'<img src = {obj.image.url} width = "300"')

    get_image.short_description = "Изображение"


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


class ServiceInline(StackedInline):
    model = Service
    extra = 0

class ServicePageAdmin(admin.ModelAdmin):
    inlines = [ServiceInline, ]



class ServiceAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    inlines = [ContentBlockInline, ]

    class Media:
        css = {
            "all": ("css/admin.css",)
        }


class ContentBlockAdmin(PolymorphicParentModelAdmin):
    base_model = ContentBlock
    child_models = (ImagesBlock, SliderBlock, IconsBlock, AboutService, StepBlock, Diagram)
    list_editable = ('order',)
    list_display = ('id', 'title', 'description', 'service', 'order')
    list_filter = (ServiceFilter,)


admin.site.register(ServicePage, ServicePageAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ContentBlock, ContentBlockAdmin)
admin.site.register(ImagesBlock, ImagesBlockAdmin)
admin.site.register(SliderBlock, SliderBlockAdmin)
admin.site.register(IconsBlock, IconsBlockAdmin)
admin.site.register(AboutService, AboutServiceAdmin)
admin.site.register(StepBlock, StepBlockAdmin)
admin.site.register(Diagram, DiagramBlockAdmin)

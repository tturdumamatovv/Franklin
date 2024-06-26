from django.contrib import admin
from django.contrib.admin import StackedInline
from django.utils.safestring import mark_safe

from polymorphic.admin import (
    PolymorphicInlineSupportMixin,
    StackedPolymorphicInline,
    PolymorphicParentModelAdmin,
    PolymorphicChildModelAdmin
)

from .models import (
    AboutPage,
    ContentBlock,
    ImagesBlock,
    SliderBlock,
    Image,
    Slide,
    Icon,
    IconsBlock,
    Video,
    SiteInfo
)


class ImageInline(StackedInline):
    model = Image
    extra = 0
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src = {obj.image.url} width = "300"')

    get_image.short_description = "Изображение"


class SlideInline(StackedInline):
    model = Slide
    extra = 0
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src = {obj.image.url} width = "300"')

    get_image.short_description = "Изображение"


class IconsInline(StackedInline):
    model = Icon
    extra = 0
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src = {obj.image.url} width = "300"')

    get_image.short_description = "Изображение"


class ImagesBlockAdmin(PolymorphicChildModelAdmin):
    inlines = [ImageInline, ]


class SliderBlockAdmin(PolymorphicChildModelAdmin):
    inlines = [SlideInline, ]


class IconsBlockAdmin(PolymorphicChildModelAdmin):
    inlines = [IconsInline, ]


class ImageBlockInline(StackedPolymorphicInline.Child):
    model = ImagesBlock


class SliderBlockInline(StackedPolymorphicInline.Child):
    model = SliderBlock


class IconsBlockInline(StackedPolymorphicInline.Child):
    model = IconsBlock


class ContentBlockInline(StackedPolymorphicInline):
    model = ContentBlock
    child_inlines = (
        ImageBlockInline,
        SliderBlockInline,
        IconsBlockInline,
    )


@admin.register(AboutPage)
class AboutPageAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    # inlines = [ContentBlockInline, ]
    pass


class ContentBlockAdmin(PolymorphicParentModelAdmin):
    base_model = ContentBlock
    child_models = (ImagesBlock, SliderBlock, IconsBlock)
    list_editable = ('order',)
    list_display = ('id', 'title', 'description', 'order')


@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    exclude = ('site_password', 'technical_works')



admin.site.register(ContentBlock, ContentBlockAdmin)
admin.site.register(ImagesBlock, ImagesBlockAdmin)
admin.site.register(SliderBlock, SliderBlockAdmin)
admin.site.register(IconsBlock, IconsBlockAdmin)
admin.site.register(Video)

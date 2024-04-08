from django.contrib import admin
import nested_admin
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from .models import AboutPage, TextSlider, SliderItem, BlockIcons, BLockIconsIcon, BlockImages, BlockImagesImage


class SliderItemInline(SortableInlineAdminMixin, nested_admin.NestedStackedInline):
    model = SliderItem
    extra = 0
    fk_name = 'text_slider'
    fields = ['image', 'sort_order']
    readonly_fields = ('sort_order',)


class TextSliderInline(SortableInlineAdminMixin, nested_admin.NestedStackedInline):
    model = TextSlider
    inlines = [SliderItemInline]
    extra = 0
    fields = ['name', 'title', 'text', 'duration', 'sort_order']
    readonly_fields = ('sort_order',)


class BlockIconsIconInline(SortableInlineAdminMixin, nested_admin.NestedStackedInline):
    model = BLockIconsIcon
    extra = 0
    fk_name = 'block'
    fields = ['title', 'text', 'image', 'sort_order']
    readonly_fields = ('sort_order',)


class BlockIconsInline(SortableInlineAdminMixin, nested_admin.NestedStackedInline):
    model = BlockIcons
    inlines = [BlockIconsIconInline]
    extra = 0
    fields = ['title', 'sort_order']
    readonly_fields = ('sort_order',)


class BlockImagesImageInline(SortableInlineAdminMixin, nested_admin.NestedStackedInline):
    model = BlockImagesImage
    extra = 0
    fk_name = 'block'

    fields = ['image', 'sort_order']
    readonly_fields = ('sort_order',)


class BlockImagesInline(SortableInlineAdminMixin, nested_admin.NestedStackedInline):
    model = BlockImages
    inlines = [BlockImagesImageInline]
    extra = 0
    fields = ['title', 'sub_title', 'sort_order']
    readonly_fields = ('sort_order',)


@admin.register(AboutPage)
class AboutPageAdmin(SortableAdminBase, nested_admin.NestedModelAdmin):
    inlines = [TextSliderInline, BlockIconsInline, BlockImagesInline]

    class Media:
        css = {
            "all": ("css/admin.css",)
        }

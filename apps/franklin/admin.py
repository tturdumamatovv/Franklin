import nested_admin
from django.contrib import admin
from polymorphic.admin import PolymorphicParentModelAdmin, PolymorphicChildModelAdmin

from .models import AboutPage, BasicAboutBlock, TextSlider, SliderItem, BlockIcons, BLockIconsIcon, BlockImages, \
    BlockImagesImage

#
# class SliderItemInline(nested_admin.NestedTabularInline):
#     model = SliderItem
#     fk_name = 'text_slider'
#
#     extra = 1
#
#
# class TextSliderInline(nested_admin.NestedStackedInline):
#     model = TextSlider
#     inlines = [SliderItemInline]
#     fk_name = 'block'
#
#     extra = 1
#
#
# class BlockIconsIconInline(nested_admin.NestedTabularInline):
#     model = BLockIconsIcon
#     fk_name = 'block'
#
#     extra = 1
#
#
# class BlockIconsInline(nested_admin.NestedStackedInline):
#     model = BlockIcons
#     inlines = [BlockIconsIconInline]
#     fk_name = 'block'
#     extra = 1


# class BlockImagesImageInline(nested_admin.NestedTabularInline):
#     model = BlockImagesImage
#     fk_name = 'block'
#     extra = 1


# class BlockImagesInline(nested_admin.NestedStackedInline):
#     model = BlockImages
#     inlines = [BlockImagesImageInline]
#     fk_name = 'block'
#     extra = 1
#
#
# class BasicAboutBlockInline(nested_admin.NestedStackedInline):
#     model = BasicAboutBlock
#     inlines = [TextSliderInline, BlockIconsInline, BlockImagesInline]
#     extra = 1


# @admin.register(AboutPage)
# class AboutPageAdmin(nested_admin.NestedModelAdmin):
#     inlines = [BasicAboutBlockInline]

@admin.register(TextSlider)
class TextSliderAdmin(PolymorphicChildModelAdmin):
    base_model = TextSlider
    # Настройте админ-класс как обычно

@admin.register(BlockIcons)
class BlockIconsAdmin(PolymorphicChildModelAdmin):
    base_model = BlockIcons
    # Настройте админ-класс как обычно

@admin.register(BlockImages)
class BlockImagesAdmin(PolymorphicChildModelAdmin):
    base_model = BlockImages
    # Настройте админ-класс как обычно

# Регистрация родительской модели
@admin.register(BasicAboutBlock)
class BasicAboutBlockAdmin(PolymorphicParentModelAdmin):
    base_model = BasicAboutBlock
    child_models = (TextSlider, BlockIcons, BlockImages)

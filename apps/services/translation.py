from modeltranslation.translator import register, TranslationOptions
from .models import (ServicePage, ContentBlock, IconsBlock, Icon, SliderBlock, Slide,
                     StepBlock, Step, AboutService, AboutServiceImage, ImagesBlock, Image, Diagram)

@register(ServicePage)
class ServicePageTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(ContentBlock)
class ContentBlockTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(Icon)
class IconTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title',)

@register(StepBlock)
class StepBlockTranslationOptions(TranslationOptions):
    fields = ('sub_title',)

@register(Step)
class StepTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

@register(AboutService)
class AboutServiceTranslationOptions(TranslationOptions):
    fields = ('sub_title', 'sub_sub_title', 'bonus',)


@register(Diagram)
class DiagramTranslationOptions(TranslationOptions):
    fields = ('first_field', 'second_field', 'third_field', 'result_field',)


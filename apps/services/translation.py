from modeltranslation.translator import register, TranslationOptions
from .models import (ServicePage, ContentBlock, IconsBlock, Icon, SliderBlock, Service,
                     StepBlock, Step, AboutService, AboutServiceImage, ImagesBlock, Image, Diagram)


@register(ServicePage)
class ServicePageTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title')


@register(Service)
class ServicePageTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(ContentBlock)
class ContentBlockTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


@register(ImagesBlock)
class ContentBlockTranslationOptions(TranslationOptions):
    pass


@register(SliderBlock)
class ContentBlockTranslationOptions(TranslationOptions):
    pass


@register(IconsBlock)
class ContentBlockTranslationOptions(TranslationOptions):
    pass


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
    fields = ('sub_title', 'bonus',)


@register(Diagram)
class DiagramTranslationOptions(TranslationOptions):
    fields = ('first_field', 'second_field', 'third_field', 'result_field',)

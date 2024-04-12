from modeltranslation.translator import register, TranslationOptions
from .models import AboutPage, ContentBlock, ImagesBlock, SliderBlock, IconsBlock, Icon

@register(AboutPage)
class AboutPageTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title')

@register(ContentBlock)
class ContentBlockTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(ImagesBlock)
class ImagesBlockTranslationOptions(TranslationOptions):
    pass

@register(SliderBlock)
class SliderBlockTranslationOptions(TranslationOptions):
    pass

@register(IconsBlock)
class IconsBlockTranslationOptions(TranslationOptions):
    pass

@register(Icon)
class IconTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title')

from modeltranslation.translator import register, TranslationOptions
from .models import PortfolioPage, PortfolioDuration, PortfolioProject, PortfolioImage

@register(PortfolioPage)
class PortfolioPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)  # Specify which fields should be translatable

@register(PortfolioDuration)
class PortfolioDurationTranslationOptions(TranslationOptions):
    fields = ('name',)  # Only 'name' is translatable

@register(PortfolioProject)
class PortfolioProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'location',)  # Multiple fields to translate

# Since PortfolioImage does not contain any translatable text fields,
# we do not need to register it for translations unless you decide
# to store some textual metadata in the future.

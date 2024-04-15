from modeltranslation.translator import register, TranslationOptions
from .models import Contact, Address, SocialLink

@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Address)
class AddressTranslationOptions(TranslationOptions):
    fields = ('address',)

@register(SocialLink)
class SocialLinkTranslationOptions(TranslationOptions):
    fields = ('link',)


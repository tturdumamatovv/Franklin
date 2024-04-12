from modeltranslation.translator import register, TranslationOptions
from .models import Contact, Address, Phone, Email, SocialLink, Application


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title')


@register(Address)
class AddressTranslationOptions(TranslationOptions):
    fields = ('address',)


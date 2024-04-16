from modeltranslation.translator import register, TranslationOptions
from .models import Contact, Address


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title')


@register(Address)
class AddressTranslationOptions(TranslationOptions):
    fields = ('address',)


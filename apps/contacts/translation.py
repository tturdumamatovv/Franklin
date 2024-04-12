from modeltranslation.translator import register, TranslationOptions
from .models import Contact, Address, Phone, Email, SocialLink, Application

@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('title',)

@register(Address)
class AddressTranslationOptions(TranslationOptions):
    fields = ('address',)

@register(Phone)
class PhoneTranslationOptions(TranslationOptions):
    fields = ('phone',)

@register(Email)
class EmailTranslationOptions(TranslationOptions):
    fields = ('email',)

@register(SocialLink)
class SocialLinkTranslationOptions(TranslationOptions):
    fields = ('link',)

@register(Application)
class ApplicationTranslationOptions(TranslationOptions):
    fields = ('name', 'phone', 'message',)

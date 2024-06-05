from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.about_us.models import SingletonModel


class Contact(SingletonModel):
    title = models.CharField(max_length=120, verbose_name=_('Заголовок'))
    sub_title = models.CharField(max_length=200, verbose_name=_('Подзаголовок'), blank=True, null=True)
    pop_message = models.CharField(max_length=200, blank=True, null=True, verbose_name=_("Всплывающие сообщение"))
    pop_icon = models.FileField(upload_to='pip_icon', blank=True, null=True
                                , verbose_name=_("Иконка всплывающего сообщения"))
    pop_title = models.CharField(max_length=200, blank=True, null=True
                                 , verbose_name=_("Заголовок всплывающего сообщения"))

    class Meta:
        verbose_name = _('Страница "Контакты"')
        verbose_name_plural = _('Страница "Контакты"')

    def __str__(self):
        return 'Контакты'


class Address(models.Model):
    address = models.CharField(max_length=200, verbose_name=_('Адрес'))
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='addresses')

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = _('Адрес')
        verbose_name_plural = _('Адреса')


class Phone(models.Model):
    phone = models.CharField(max_length=200, verbose_name=_('Телефон'))
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='phones')

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = _('Телефон')
        verbose_name_plural = _('Телефоны')


class Email(models.Model):
    email = models.EmailField(max_length=200, verbose_name=_('Электронная почта'))
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='emails')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('Почта')
        verbose_name_plural = _('Почты')


class SocialLink(models.Model):
    link = models.URLField(max_length=200, verbose_name=_('Ссылка'))
    icon = models.FileField(upload_to='social_icons', verbose_name='Иконка')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='social_links')

    def __str__(self):
        return f'{self.link}' or 'Social Link'

    class Meta:
        verbose_name = _('Социальная сеть')
        verbose_name_plural = _('Социальные сети')


class Application(models.Model):
    name = models.CharField(max_length=120, verbose_name=_('Имя'))
    phone = models.CharField(max_length=100, verbose_name=_("Номер телефона"))
    message = models.TextField(verbose_name=_('Сообщение'), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name=_("Дата заявки"))

    class Meta:
        verbose_name = _('Заявка')
        verbose_name_plural = _('Заявки')


class Preload(SingletonModel):
    logo = models.FileField(upload_to='preload_logo/')
    image = models.ImageField(upload_to='preload/', verbose_name=_('Изображение'))
    text = models.CharField(max_length=250, verbose_name=_('Текст'))

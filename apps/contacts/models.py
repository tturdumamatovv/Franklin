from django.db import models
from django.utils.translation import gettext_lazy as _


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.__class__.objects.exists():
            existing_instance = self.__class__.objects.get()
            if self.id != existing_instance.id:
                for field in self._meta.fields:
                    if field.name != "id":
                        setattr(existing_instance, field.name, getattr(self, field.name))
                existing_instance.save(*args, **kwargs)
        else:
            super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        if not cls.objects.exists():
            cls.objects.create()
        return cls.objects.get()


class Contact(SingletonModel):
    title = models.CharField(max_length=120, verbose_name=_('Заголовок'))

    def __str__(self):
        return self.title


class Address(models.Model):
    address = models.CharField(max_length=200, verbose_name=_('Адрес'))
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='addresses')

    def __str__(self):
        return self.address


class Phone(models.Model):
    phone = models.CharField(max_length=200, verbose_name=_('Телефон'))
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='phones')

    def __str__(self):
        return self.phone


class Email(models.Model):
    email = models.EmailField(max_length=200, verbose_name=_('Электронная почта'))
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='emails')

    def __str__(self):
        return self.email


class SocialLink(models.Model):
    link = models.URLField(max_length=200, verbose_name=_('Ссылка'))
    icon = models.ImageField(upload_to='social_icons', verbose_name='Иконка')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='social_links')

    def __str__(self):
        return self.contact


class Application(models.Model):
    name = models.CharField(max_length=120, verbose_name=_('Имя'))
    phone = models.CharField(max_length=100, verbose_name=_("Номер телефона"))
    message = models.TextField(verbose_name=_('Сообщение'))

    def __str__(self):
        return self.name

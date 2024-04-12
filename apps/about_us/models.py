from django.db import models
from django.utils.translation import gettext_lazy as _

from ckeditor.fields import RichTextField
from polymorphic.models import PolymorphicModel


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


class AboutPage(SingletonModel):
    title = models.CharField(max_length=200, verbose_name=_('Заголовок'))
    sub_title = models.CharField(max_length=200, verbose_name=_('Подзаголовок'), blank=True, null=True)

    class Meta:
        verbose_name = _('Страница "О Нас"')
        verbose_name_plural = _('Страница "О Нас"')

    def __str__(self):
        return self.title


class ContentBlock(PolymorphicModel):
    page = models.ForeignKey(AboutPage, on_delete=models.CASCADE, related_name='content_blocks',
                             verbose_name=_('Страница'))
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name=_('Порядок'))
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Заголовок'))
    description = RichTextField(blank=True, null=True, verbose_name=_('Описание'))

    class Meta:
        ordering = ['order']
        verbose_name = _('Блок')
        verbose_name_plural = _('Блоки')

    def __str__(self):
        return f"{self.title}"


class ImagesBlock(ContentBlock):
    type = 'images'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Блок с картинками')
        verbose_name_plural = _('Блоки с картинками')


class Image(models.Model):
    image = models.ImageField(upload_to='about_page')
    block = models.ForeignKey(ImagesBlock, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = _('Картинка')
        verbose_name_plural = _('Картинки')


class SliderBlock(ContentBlock):
    type = 'slider'
    duration = models.CharField(max_length=100 ,choices=((1, 'right'), (2, 'left')), blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Блок со слайдером')
        verbose_name_plural = _('Блоки со слайдером')


class Slide(models.Model):
    image = models.ImageField(upload_to='about_slide')
    block = models.ForeignKey(SliderBlock, on_delete=models.CASCADE, related_name='slides')

    class Meta:
        verbose_name = _('Слайд')
        verbose_name_plural = _('Слайды')


class IconsBlock(ContentBlock):
    type = 'icons'

    class Meta:
        verbose_name = _('Блок с иконками')
        verbose_name_plural = _('Блоки с иконками')

    def __str__(self):
        return self.title


class Icon(models.Model):
    image = models.ImageField(upload_to='icons/')
    title = models.CharField(max_length=30)
    sub_title = models.CharField(max_length=50, blank=True, null=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name=_('Порядок'))
    block = models.ForeignKey(IconsBlock, on_delete=models.CASCADE, related_name='icons')

    class Meta:
        ordering = ['order']
        verbose_name = _('Иконка')
        verbose_name_plural = _('Иконки')

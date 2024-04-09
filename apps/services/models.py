from ckeditor.fields import RichTextField
from django.db import models
from polymorphic.models import PolymorphicModel
from django.utils.translation import gettext_lazy as _

from apps.about_us.models import SingletonModel


class ServicePage(SingletonModel):
    name = models.CharField(max_length=150, verbose_name=_('Название'))

    class Meta:
        verbose_name = _('Страница "Услуги"')
        verbose_name_plural = _('Страница "Услуги"')

    def __str__(self):
        return self.name


class ContentBlock(PolymorphicModel):
    page = models.ForeignKey(ServicePage, on_delete=models.CASCADE, related_name='content_blocks',
                             verbose_name=_('Страница'))
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name=_('Порядок'))
    title = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Заголовок'))
    description = RichTextField(blank=True, null=True, verbose_name=_('Описание'))

    class Meta:
        ordering = ['order']
        verbose_name = _('Блок')
        verbose_name_plural = _('Блоки')

    def __str__(self):
        return self.title


class IconsBlock(ContentBlock):
    class Meta:
        verbose_name = _('Блок с иконками')
        verbose_name_plural = _('Блоки с иконками')

    def __str__(self):
        return self.title


class Icon(models.Model):
    image = models.ImageField(upload_to='icon/', verbose_name=_('Изображение'))
    title = models.CharField(max_length=30, verbose_name=_('Заголовок'))
    sub_title = models.CharField(max_length=50, verbose_name=_('Подзаголовок'))
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name=_('Порядок'))
    block = models.ForeignKey(IconsBlock, on_delete=models.CASCADE, related_name='icons')

    class Meta:
        ordering = ['order']
        verbose_name = _('Иконка')
        verbose_name_plural = _('Иконки')


class SliderBlock(ContentBlock):

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Блок со слайдером')
        verbose_name_plural = _('Блоки со слайдером')


class Slide(models.Model):
    image = models.ImageField(upload_to='slide/', verbose_name=_('Изображение'))
    block = models.ForeignKey(SliderBlock, on_delete=models.CASCADE, related_name='slides')

    class Meta:
        verbose_name = _('Слайд')
        verbose_name_plural = _('Слайды')


class StepBlock(ContentBlock):
    sub_title = models.CharField(max_length=150, verbose_name=_('Подзаголовок'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Блок со слайдером')
        verbose_name_plural = _('Блоки со слайдером')


class Step(models.Model):
    image = models.ImageField(upload_to='step/', verbose_name=_('Изображение'))
    title = models.CharField(max_length=150, verbose_name=_('Заголовок'))
    description = models.TextField(verbose_name=_('Описание'))
    block = models.ForeignKey(StepBlock, on_delete=models.CASCADE, related_name='steps')

    class Meta:
        verbose_name = _('Слайд')
        verbose_name_plural = _('Слайды')


class AboutService(ContentBlock):
    sub_title = models.CharField(max_length=150, verbose_name=_('Подзаголовок'))
    sub_sub_title = models.CharField(max_length=150, verbose_name=_('Под-подзаголовок'))
    bonus = models.CharField(max_length=150, verbose_name=_('Бонус'))

    def __str__(self):
        return self.title


class AboutServiceImage(models.Model):
    image = models.ImageField(upload_to='about_services/', verbose_name=_('Изображение'))
    block = models.ForeignKey(AboutService, on_delete=models.CASCADE, related_name='images')


class ImagesBlock(ContentBlock):

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='services/', verbose_name=_('Изображение'))
    block = models.ForeignKey(ImagesBlock, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = _('Картинка')
        verbose_name_plural = _('Картинки')

from ckeditor.fields import RichTextField
from django.db import models
from polymorphic.models import PolymorphicModel
from django.utils.translation import gettext_lazy as _


class ServicePage(models.Model):
    name = models.CharField(max_length=150)


class Service(models.Model):
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    service_page = models.ForeignKey(ServicePage, on_delete=models.PROTECT)


class ServiceImage(models.Model):
    image = models.ImageField(upload_to='services/')
    service = models.ForeignKey(Service, on_delete=models.CASCADE)


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


class IconsBlock(ContentBlock):
    class Meta:
        verbose_name = _('Блок с иконками')
        verbose_name_plural = _('Блоки с иконками')

    def __str__(self):
        return self.title


class Icon(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=30)
    sub_title = models.CharField(max_length=50)
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
    image = models.ImageField()
    block = models.ForeignKey(SliderBlock, on_delete=models.CASCADE, related_name='categories')

    class Meta:
        verbose_name = _('Слайд')
        verbose_name_plural = _('Слайды')


class StepBlock(ContentBlock):
    sub_title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Блок со слайдером')
        verbose_name_plural = _('Блоки со слайдером')


class Step(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=150)
    description = models.TextField()
    block = models.ForeignKey(SliderBlock, on_delete=models.CASCADE, related_name='categories')

    class Meta:
        verbose_name = _('Слайд')
        verbose_name_plural = _('Слайды')


class AboutService(ContentBlock):
    sub_title = models.CharField(max_length=150)
    sub_sub_title = models.CharField(max_length=150)
    bonus = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Блок с картинками')
        verbose_name_plural = _('Блоки с картинками')


class AboutServiceImage(models.Model):
    image = models.ImageField()
    block = models.ForeignKey(AboutService, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = _('Картинка')
        verbose_name_plural = _('Картинки')

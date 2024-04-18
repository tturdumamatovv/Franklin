from ckeditor.fields import RichTextField
from django.db import models
from polymorphic.models import PolymorphicModel
from django.utils.translation import gettext_lazy as _

from apps.about_us.models import SingletonModel


class ServicePage(SingletonModel):
    title = models.CharField(max_length=150, verbose_name=_('Заголовок'))
    sub_title = models.CharField(max_length=200, verbose_name=_('Подзаголовок'), blank=True, null=True)

    class Meta:
        verbose_name = _('Страница "Услуги"')
        verbose_name_plural = _('Страница "Услуги"')

    def __str__(self):
        return 'Страница "Услуги"'


class Service(models.Model):
    page = models.ForeignKey(ServicePage, on_delete=models.CASCADE, related_name='services',
                             verbose_name=_('Страница'))
    title = models.CharField(max_length=100, verbose_name=_('Заголовок'))
    image = models.ImageField(upload_to='services/', verbose_name=_('Изображение'))

    def __str__(self):
        return self.title or f'сервис {self.id}'


class ContentBlock(PolymorphicModel):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='content_blocks',
                             verbose_name=_('Сервис'))
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
    type = models.CharField(max_length=20, default='principes', auto_created=True, editable=False)

    class Meta:
        verbose_name = _('Блок с иконками')
        verbose_name_plural = _('Блоки с иконками')

    def __str__(self):
        return self.title


class Icon(models.Model):
    image = models.ImageField(upload_to='icon/', verbose_name=_('Изображение'))
    title = models.CharField(max_length=30, verbose_name=_('Заголовок'), blank=True, null=True)
    sub_title = models.CharField(max_length=50, verbose_name=_('Подзаголовок'), blank=True, null=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name=_('Порядок'))
    block = models.ForeignKey(IconsBlock, on_delete=models.CASCADE, related_name='icons')

    class Meta:
        ordering = ['order']
        verbose_name = _('Иконка')
        verbose_name_plural = _('Иконки')


class SliderBlock(ContentBlock):
    duration = models.CharField(max_length=20,choices=(('right', 'right'), ('left', 'left')), blank=True, null=True)
    uppercase = models.BooleanField(default=False)
    type = models.CharField(max_length=10, default='slider', auto_created=True, editable=False)

    def __str__(self):
        return self.title or self.type

    class Meta:
        verbose_name = _('Блок со слайдером')
        verbose_name_plural = _('Блоки со слайдером')

    def save(self, *args, **kwargs):
        if self.uppercase:
            self.type = 'subtelties'
        elif not self.title:
            self.type = 'philosophy'
        else:
            self.type = 'about'
        super().save(*args, **kwargs)


class Slide(models.Model):
    image = models.ImageField(upload_to='slide/', verbose_name=_('Изображение'))
    block = models.ForeignKey(SliderBlock, on_delete=models.CASCADE, related_name='slides')

    class Meta:
        verbose_name = _('Слайд')
        verbose_name_plural = _('Слайды')


class StepBlock(ContentBlock):
    type = models.CharField(max_length=20, default='service-plan', auto_created=True, editable=False)
    sub_title = models.CharField(max_length=150, verbose_name=_('Подзаголовок'), blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Блок со слайдером')
        verbose_name_plural = _('Блоки со слайдером')


class Step(models.Model):
    image = models.ImageField(upload_to='step/', verbose_name=_('Изображение'), blank=True, null=True)
    title = models.CharField(max_length=150, verbose_name=_('Заголовок'), blank=True, null=True)
    description = models.TextField(verbose_name=_('Описание'), blank=True, null=True)
    block = models.ForeignKey(StepBlock, on_delete=models.CASCADE, related_name='steps')

    class Meta:
        verbose_name = _('Слайд')
        verbose_name_plural = _('Слайды')


class AboutService(ContentBlock):
    type = models.CharField(max_length=20, default='equipment', auto_created=True, editable=False)
    sub_title = models.CharField(max_length=150, verbose_name=_('Подзаголовок'))
    sub_sub_title = models.CharField(max_length=150, verbose_name=_('Под-подзаголовок'))
    bonus = models.CharField(max_length=150, verbose_name=_('Бонус'))

    class Meta:
        verbose_name = 'О сервисе'

    def __str__(self):
        return self.title


class AboutServiceImage(models.Model):
    image = models.ImageField(upload_to='about_services/', verbose_name=_('Изображение'))
    block = models.ForeignKey(AboutService, on_delete=models.CASCADE, related_name='images')


class ImagesBlock(ContentBlock):
    type = models.CharField(max_length=20, default='quote', auto_created=True, editable=False)

    def __str__(self):
        return self.title or self.type

    class Meta:
        verbose_name = _('Блок с картинками')
        verbose_name_plural = _('Блок с картинками')


class Image(models.Model):
    image = models.ImageField(upload_to='services/', verbose_name=_('Изображение'))
    block = models.ForeignKey(ImagesBlock, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = _('Картинка')
        verbose_name_plural = _('Картинки')


class Diagram(ContentBlock):
    first_field = models.CharField(max_length=150, verbose_name=_('Первое поле'))
    second_field = models.CharField(max_length=150, verbose_name=_('Второе поле'))
    third_field = models.CharField(max_length=150, verbose_name=_('Треье поле'))
    result_field = models.CharField(max_length=150, verbose_name=_('Результат'))
    type = 'diagram'

    class Meta:
        verbose_name = _('Диаграмма')
        verbose_name_plural = _('Диаграммы')

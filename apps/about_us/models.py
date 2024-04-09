from ckeditor.fields import RichTextField
from django.db import models
from polymorphic.models import PolymorphicModel
from django.utils.translation import gettext_lazy as _


class SingletonModel(models.Model):
    """
    Модель, которая всегда имеет только один экземпляр.
    """

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # Если модель уже существует, удалите ее
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        # Если модель еще не существует, создайте ее
        if not cls.objects.exists():
            cls.objects.create()
        return cls.objects.get()


class AboutPage(SingletonModel):
    title = models.CharField(max_length=200, verbose_name=_('Заголовок'))
    sub_title = models.CharField(max_length=200, verbose_name=_('Заголовок'))

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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Блок с картинками')
        verbose_name_plural = _('Блоки с картинками')


class Image(models.Model):
    image = models.ImageField()
    block = models.ForeignKey(ImagesBlock, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = _('Картинка')
        verbose_name_plural = _('Картинки')


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


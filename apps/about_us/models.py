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
    type = models.CharField(max_length=20, default='quote', auto_created=True, editable=False)

    def __str__(self):
        return self.title or self.type

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
    type = models.CharField(max_length=20, default='slider', auto_created=True, editable=False)
    duration = models.CharField(max_length=20,choices=(('right', 'right'), ('left', 'left')), blank=True, null=True)
    uppercase = models.BooleanField(default=False)


    def __str__(self):
        return self.title

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
    image = models.ImageField(upload_to='about_slide')
    block = models.ForeignKey(SliderBlock, on_delete=models.CASCADE, related_name='slides')

    class Meta:
        verbose_name = _('Слайд')
        verbose_name_plural = _('Слайды')


class IconsBlock(ContentBlock):
    type = models.CharField(max_length=20, default='Icons', auto_created=True, editable=False)

    class Meta:
        verbose_name = _('Блок с иконками')
        verbose_name_plural = _('Блоки с иконками')

    def __str__(self):
        return self.title


class Icon(models.Model):
    image = models.FileField(upload_to='icons/')
    title = models.CharField(max_length=30)
    sub_title = models.CharField(max_length=50, blank=True, null=True)
    order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name=_('Порядок'))
    block = models.ForeignKey(IconsBlock, on_delete=models.CASCADE, related_name='icons')

    class Meta:
        ordering = ['order']
        verbose_name = _('Иконка')
        verbose_name_plural = _('Иконки')

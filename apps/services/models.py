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
        if self.__class__.objects.exists():  # Проверяем, существует ли экземпляр
            # Получаем существующий экземпляр
            existing_instance = self.__class__.objects.get()
            # Если мы не работаем с уже существующим экземпляром
            if self.id != existing_instance.id:
                # Обновляем существующий экземпляр полями из текущего экземпляра
                for field in self._meta.fields:
                    if field.name != "id":  # Пропускаем поле id
                        setattr(existing_instance, field.name, getattr(self, field.name))
                existing_instance.save(*args, **kwargs)  # Сохраняем существующий экземпляр
        else:
            # Если экземпляр не существует, просто сохраняем текущий
            super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        if not cls.objects.exists():
            cls.objects.create()
        return cls.objects.get()


class ServicePage(SingletonModel):
    name = models.CharField(max_length=150)

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
    block = models.ForeignKey(SliderBlock, on_delete=models.CASCADE, related_name='slides')

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
    block = models.ForeignKey(StepBlock, on_delete=models.CASCADE, related_name='steps')

    class Meta:
        verbose_name = _('Слайд')
        verbose_name_plural = _('Слайды')


class AboutService(ContentBlock):
    sub_title = models.CharField(max_length=150)
    sub_sub_title = models.CharField(max_length=150)
    bonus = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class AboutServiceImage(models.Model):
    image = models.ImageField()
    block = models.ForeignKey(AboutService, on_delete=models.CASCADE, related_name='images')


class ImagesBlock(ContentBlock):

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField()
    block = models.ForeignKey(ImagesBlock, on_delete=models.CASCADE, related_name='images')

    class Meta:
        verbose_name = _('Картинка')
        verbose_name_plural = _('Картинки')


from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.__class__.objects.exclude(id=self.id).delete()
        super(SingletonModel, self).save(*args, **kwargs)

    @classmethod
    def load(cls):
        if not cls.objects.exists():
            cls.objects.create()
        return cls.objects.get()


class HomePage(SingletonModel):
    pass


class AboutPage(SingletonModel):
    title = models.CharField(max_length=100, verbose_name=_('Заголовок'))
    text = RichTextField(verbose_name=_('Описание'))

    def __str__(self):
        return self.title


class TextSlider(models.Model):
    CHOOSE_DURATION = (
        (1, "Left"),
        (2, "Right")
    )

    name = models.CharField(max_length=100, verbose_name=_('Название'))
    title = models.CharField(max_length=100, verbose_name=_('Заголовок'), null=True, blank=True)
    text = RichTextField(verbose_name=_('Описание'))
    duration = models.CharField(max_length=100, choices=CHOOSE_DURATION)

    def __str__(self):
        return self.name


class SliderItem(models.Model):
    image = models.ImageField(upload_to='sliders/')
    text_slider = models.ForeignKey(TextSlider, on_delete=models.CASCADE)


class BlockIcons(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Заголовок'))


class BLockIconsIcon(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Заголовок'))
    text = models.CharField(max_length=100, verbose_name=_('Описание'))
    image = models.ImageField(upload_to='icons/')
    block = models.ForeignKey(BlockIcons, on_delete=models.CASCADE)


class BlockImages(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Заголовок'))
    sub_title = models.CharField(max_length=100, verbose_name=_('Подзаголовок'))


class BlockImagesImage(models.Model):
    image = models.ImageField(upload_to='images/')
    block = models.ForeignKey(BlockImages, on_delete=models.CASCADE)


class PortfolioPage(SingletonModel):
    pass


class ServicePage(SingletonModel):
    pass


class ContactPage(SingletonModel):
    pass

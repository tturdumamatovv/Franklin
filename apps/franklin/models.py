from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from polymorphic.models import PolymorphicModel



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


class SortableModel(models.Model):
    sort_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)


    class Meta:
        ordering = ['sort_order']


class BasicAboutBlock(PolymorphicModel, SortableModel):
    about_page = models.ForeignKey(AboutPage, on_delete=models.CASCADE)


class TextSlider(BasicAboutBlock):
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


class SliderItem(SortableModel):
    image = models.ImageField(upload_to='sliders/')
    text_slider = models.ForeignKey(TextSlider, on_delete=models.CASCADE)


class BlockIcons(BasicAboutBlock):
    title = models.CharField(max_length=100, verbose_name=_('Заголовок'))


class BLockIconsIcon(SortableModel):
    title = models.CharField(max_length=100, verbose_name=_('Заголовок'))
    text = models.CharField(max_length=100, verbose_name=_('Описание'))
    image = models.ImageField(upload_to='block_icons/')
    block = models.ForeignKey(BlockIcons, on_delete=models.CASCADE)


class BlockImages(BasicAboutBlock):
    title = models.CharField(max_length=100, verbose_name=_('Заголовок'))
    sub_title = models.CharField(max_length=100, verbose_name=_('Подзаголовок'))


class BlockImagesImage(SortableModel):
    image = models.ImageField(upload_to='block_images/')
    block = models.ForeignKey(BlockImages, on_delete=models.CASCADE)


class PortfolioPage(SingletonModel):
    pass


class PortfolioDuration(models.Model):
    image = models.ImageField(upload_to='portfolio_images')
    title = models.CharField(max_length=100, verbose_name=_('Заголовок'))
    # portfolio = models.ForeignKey()


class PortfolioProject(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('Заголовок'))


class ServicePage(SingletonModel):
    pass


class ContactPage(SingletonModel):
    pass

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from unidecode import unidecode

from apps.about_us.models import SingletonModel


class PortfolioPage(SingletonModel):
    title = models.CharField(max_length=200, verbose_name=_('Заголовок'))
    sub_title = models.CharField(max_length=200, verbose_name=_('Подзаголовок'), blank=True, null=True)

    class Meta:
        verbose_name = _('Страница "Портфолио"')
        verbose_name_plural = _('Страница "Портфолио"')

    def __str__(self):
        return 'Страница "Портфолио"'


class PortfolioDuration(models.Model):
    page = models.ForeignKey(PortfolioPage, related_name='durations', on_delete=models.CASCADE
                             , verbose_name=_("Страница"))
    image = models.ImageField(upload_to='portfolio_duration/', verbose_name=_("Изображение"))
    name = models.CharField(max_length=150, verbose_name=_('Название'))
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(unidecode(self.name))
            unique_slug = base_slug
            counter = 1

            while PortfolioDuration.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = unique_slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Направление проекта')
        verbose_name_plural = _('Направление проектов')



class PortfolioProject(models.Model):
    duration = models.ForeignKey(PortfolioDuration, related_name='projects', on_delete=models.CASCADE
                                 , verbose_name=_("Направление"))
    title = models.CharField(max_length=150, verbose_name=_('Заголовок'))
    description = models.TextField(verbose_name=_('Описание'), blank=True, null=True)
    location = models.CharField(max_length=150, verbose_name=_('Локация'))
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name=_('Слоган[en]'))
    keywords = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Ключевые слова'))
    meta_title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Мета-заголовок'))
    meta_description = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('Мета-описание'))
    meta_image = models.FileField(upload_to='meta_images', blank=True, null=True, default='static/icons/LOGO.svg'
                                  , verbose_name=_('Мета-изображение'))
    order = models.IntegerField(default=0, verbose_name=_('Порядок'), blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(unidecode(self.title))
            unique_slug = base_slug
            counter = 1

            while PortfolioDuration.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = unique_slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Портфолио проекта')
        verbose_name_plural = _('Портфолио проектов')
        ordering = ['order']



class PortfolioImage(models.Model):
    project = models.ForeignKey(PortfolioProject, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio_projects/', verbose_name=_("Изображение"))

    def __str__(self):
        return f"Изображение для - {self.project.title}"

    class Meta:
        verbose_name = _('Изображения портфолио')
        verbose_name_plural = _('Изображении портфолио')

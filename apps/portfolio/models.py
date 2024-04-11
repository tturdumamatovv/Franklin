from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.about_us.models import SingletonModel


class PortfolioPage(SingletonModel):
    title = models.CharField(max_length=200, verbose_name=_('Загловок'))
    content = models.TextField(verbose_name=_('Контент'), blank=True, null=True)

    def __str__(self):
        return self.title


class PortfolioDuration(models.Model):
    page = models.ForeignKey(PortfolioPage, related_name='durations', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio_duration/')
    name = models.CharField(max_length=150, verbose_name=_('Название'))

    def __str__(self):
        return self.name


class PortfolioProject(models.Model):
    duration = models.ForeignKey(PortfolioDuration, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=150, verbose_name=_('Заголовок'))
    description = models.TextField(verbose_name=_('Описание'), blank=True, null=True)
    location = models.CharField(max_length=150, verbose_name=_('Локация'))

    def __str__(self):
        return self.title


class PortfolioImage(models.Model):
    project = models.ForeignKey(PortfolioProject, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio_projects/')

    def __str__(self):
        return f"Image for {self.project.title}"

from django.db import models
from polymorphic.models import PolymorphicModel


class PortfolioPage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class ContentBlock(PolymorphicModel):
    page = models.ForeignKey(PortfolioPage, on_delete=models.CASCADE, related_name='content_blocks')
    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    title = models.CharField(max_length=200, blank=True)
    description = models.TextField()


    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.title}"


class ImagesBlock(ContentBlock):

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField()
    block = models.ForeignKey(ImagesBlock, on_delete=models.CASCADE, related_name='images')


class SliderBlock(ContentBlock):

    def __str__(self):
        return self.title


class Slide(models.Model):
    image = models.ImageField()
    block = models.ForeignKey(SliderBlock, on_delete=models.CASCADE, related_name='categories')

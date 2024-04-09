from django.db import models


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


class PortfolioPage(SingletonModel):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def str(self):
        return self.title


class PortfolioDuration(models.Model):
    image = models.ImageField(upload_to='portfolio_duration/')
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class PortfolioProject(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    location = models.CharField(max_length=150)
    duration = models.ForeignKey(PortfolioDuration, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class PortfolioImage(models.Model):
    image = models.ImageField(upload_to='portfolio_projects/')
    project = models.ForeignKey(PortfolioProject, related_name='images', on_delete=models.CASCADE)

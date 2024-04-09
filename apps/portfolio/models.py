from django.db import models


class PortfolioPage(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def str(self):
        return self.title


class PortfolioDuration(models.Model):
    image = models.ImageField(upload_to='portfolio_duration/')
    name = models.CharField(max_length=150)


class PortfolioProject(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    location = models.CharField(max_length=150)


class PortfolioImage(models.Model):
    image = models.ImageField(upload_to='portfolio_projects/')
    project = models.ForeignKey(PortfolioProject, on_delete=models.CASCADE)
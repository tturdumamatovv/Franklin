# Generated by Django 5.0.4 on 2024-06-05 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_portfolioduration_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliopage',
            name='meta_image',
            field=models.FileField(blank=True, default='static/icons/LOGO.svg', null=True, upload_to='meta_images', verbose_name='Мета-изображение'),
        ),
        migrations.AlterField(
            model_name='portfolioproject',
            name='keywords',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ключевые слова'),
        ),
        migrations.AlterField(
            model_name='portfolioproject',
            name='meta_image',
            field=models.FileField(blank=True, default='static/icons/LOGO.svg', null=True, upload_to='meta_images', verbose_name='Мета-изображение'),
        ),
        migrations.AlterField(
            model_name='portfolioproject',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='Слоган[en]'),
        ),
    ]

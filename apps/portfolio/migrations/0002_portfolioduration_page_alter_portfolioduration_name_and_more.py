# Generated by Django 5.0.4 on 2024-04-09 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolioduration',
            name='page',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='durations', to='portfolio.portfoliopage'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='portfolioduration',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='portfoliopage',
            name='content',
            field=models.TextField(verbose_name='Контент'),
        ),
        migrations.AlterField(
            model_name='portfoliopage',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Загловок'),
        ),
        migrations.AlterField(
            model_name='portfolioproject',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='portfolioproject',
            name='duration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='portfolio.portfolioduration'),
        ),
        migrations.AlterField(
            model_name='portfolioproject',
            name='location',
            field=models.CharField(max_length=150, verbose_name='Локация'),
        ),
        migrations.AlterField(
            model_name='portfolioproject',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Описание'),
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-16 09:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Загловок')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Загловок')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='Загловок')),
                ('sub_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Подзаголовок')),
                ('sub_title_en', models.CharField(blank=True, max_length=200, null=True, verbose_name='Подзаголовок')),
                ('sub_title_ru', models.CharField(blank=True, max_length=200, null=True, verbose_name='Подзаголовок')),
            ],
            options={
                'verbose_name': 'Страница "Портфолио"',
                'verbose_name_plural': 'Страница "Портфолио"',
            },
        ),
        migrations.CreateModel(
            name='PortfolioDuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio_duration/')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('name_en', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('name_ru', models.CharField(max_length=150, null=True, verbose_name='Название')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='durations', to='portfolio.portfoliopage')),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('title_en', models.CharField(max_length=150, null=True, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=150, null=True, verbose_name='Заголовок')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('location', models.CharField(max_length=150, verbose_name='Локация')),
                ('location_en', models.CharField(max_length=150, null=True, verbose_name='Локация')),
                ('location_ru', models.CharField(max_length=150, null=True, verbose_name='Локация')),
                ('duration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='portfolio.portfolioduration')),
            ],
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='portfolio_projects/')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='portfolio.portfolioproject')),
            ],
        ),
    ]

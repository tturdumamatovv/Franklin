# Generated by Django 5.0.4 on 2024-04-25 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0005_siteinfo_site_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentblock',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='contentblock',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='contentblock',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
# Generated by Django 5.0.4 on 2024-04-16 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0002_aboutpage_sub_title_ru_aboutpage_title_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='preload',
            field=models.BooleanField(default=False),
        ),
    ]
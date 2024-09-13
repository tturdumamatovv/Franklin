# Generated by Django 5.0.4 on 2024-09-13 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_alter_portfolioproject_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfolioimage',
            options={'ordering': ['order'], 'verbose_name': 'Изображения портфолио', 'verbose_name_plural': 'Изображении портфолио'},
        ),
        migrations.AddField(
            model_name='portfolioimage',
            name='order',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Порядок'),
        ),
    ]
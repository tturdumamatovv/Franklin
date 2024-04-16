# Generated by Django 5.0.4 on 2024-04-16 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_address_address_ru_contact_sub_title_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sociallink',
            name='link_en',
            field=models.URLField(null=True, verbose_name='Ссылка'),
        ),
        migrations.AddField(
            model_name='sociallink',
            name='link_ru',
            field=models.URLField(null=True, verbose_name='Ссылка'),
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-01 09:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0006_alter_contentblock_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentblock',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='contentblock',
            name='description_en',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='contentblock',
            name='description_ru',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-17 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_preload_remove_sociallink_link_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='pop_icon',
            field=models.FileField(blank=True, null=True, upload_to='pip_icon'),
        ),
        migrations.AddField(
            model_name='contact',
            name='pop_message',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='pop_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

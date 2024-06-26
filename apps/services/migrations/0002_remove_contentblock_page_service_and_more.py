# Generated by Django 5.0.4 on 2024-04-17 04:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contentblock',
            name='page',
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='services/', verbose_name='Изображение')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='services.servicepage', verbose_name='Страница')),
            ],
        ),
        migrations.AddField(
            model_name='contentblock',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='content_blocks', to='services.service', verbose_name='Сервис'),
            preserve_default=False,
        ),
    ]

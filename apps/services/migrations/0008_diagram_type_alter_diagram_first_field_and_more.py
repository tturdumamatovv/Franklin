# Generated by Django 5.0.4 on 2024-04-18 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_remove_aboutservice_sub_sub_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagram',
            name='type',
            field=models.CharField(auto_created=True, default='offer', editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='diagram',
            name='first_field',
            field=models.CharField(max_length=150, verbose_name='Верхнее поле'),
        ),
        migrations.AlterField(
            model_name='diagram',
            name='first_field_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Верхнее поле'),
        ),
        migrations.AlterField(
            model_name='diagram',
            name='first_field_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Верхнее поле'),
        ),
        migrations.AlterField(
            model_name='diagram',
            name='result_field',
            field=models.CharField(max_length=150, verbose_name='Центральное поле'),
        ),
        migrations.AlterField(
            model_name='diagram',
            name='result_field_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Центральное поле'),
        ),
        migrations.AlterField(
            model_name='diagram',
            name='result_field_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Центральное поле'),
        ),
        migrations.AlterField(
            model_name='diagram',
            name='second_field',
            field=models.CharField(max_length=150, verbose_name='Правое поле'),
        ),
        migrations.AlterField(
            model_name='diagram',
            name='second_field_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Правое поле'),
        ),
        migrations.AlterField(
            model_name='diagram',
            name='second_field_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Правое поле'),
        ),
        migrations.AlterField(
            model_name='diagram',
            name='third_field',
            field=models.CharField(max_length=150, verbose_name='Левое поле'),
        ),
        migrations.AlterField(
            model_name='diagram',
            name='third_field_en',
            field=models.CharField(max_length=150, null=True, verbose_name='Левое поле'),
        ),
        migrations.AlterField(
            model_name='diagram',
            name='third_field_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='Левое поле'),
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-09 10:02

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('sub_title', models.CharField(max_length=200, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Страница "О Нас"',
                'verbose_name_plural': 'Страница "О Нас"',
            },
        ),
        migrations.CreateModel(
            name='ContentBlock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Заголовок')),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Описание')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content_blocks', to='about_us.aboutpage', verbose_name='Страница')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
            options={
                'verbose_name': 'Блок',
                'verbose_name_plural': 'Блоки',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='IconsBlock',
            fields=[
                ('contentblock_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='about_us.contentblock')),
            ],
            options={
                'verbose_name': 'Блок с иконками',
                'verbose_name_plural': 'Блоки с иконками',
            },
            bases=('about_us.contentblock',),
        ),
        migrations.CreateModel(
            name='ImagesBlock',
            fields=[
                ('contentblock_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='about_us.contentblock')),
            ],
            options={
                'verbose_name': 'Блок с картинками',
                'verbose_name_plural': 'Блоки с картинками',
            },
            bases=('about_us.contentblock',),
        ),
        migrations.CreateModel(
            name='SliderBlock',
            fields=[
                ('contentblock_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='about_us.contentblock')),
            ],
            options={
                'verbose_name': 'Блок со слайдером',
                'verbose_name_plural': 'Блоки со слайдером',
            },
            bases=('about_us.contentblock',),
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=30)),
                ('sub_title', models.CharField(max_length=50)),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='icons', to='about_us.iconsblock')),
            ],
            options={
                'verbose_name': 'Иконка',
                'verbose_name_plural': 'Иконки',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='about_us.imagesblock')),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинки',
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='about_us.sliderblock')),
            ],
            options={
                'verbose_name': 'Слайд',
                'verbose_name_plural': 'Слайды',
            },
        ),
    ]

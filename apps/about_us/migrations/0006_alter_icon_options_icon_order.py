from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about_us', '0005_alter_aboutpage_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='icon',
            options={'ordering': ['order'], 'verbose_name': 'Иконка', 'verbose_name_plural': 'Иконки'},
        ),
        migrations.AddField(
            model_name='icon',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядок'),
        ),
    ]

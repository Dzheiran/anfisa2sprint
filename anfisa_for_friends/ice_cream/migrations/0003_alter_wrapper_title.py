# Generated by Django 4.2.10 on 2024-02-20 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ice_cream', '0002_alter_category_options_alter_icecream_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wrapper',
            name='title',
            field=models.CharField(help_text='Уникальное название обёртки, не более 256 символов', max_length=256, verbose_name='Название'),
        ),
    ]

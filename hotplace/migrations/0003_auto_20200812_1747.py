# Generated by Django 3.1 on 2020-08-12 17:47

import django.core.validators
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('hotplace', '0002_auto_20200812_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotplace',
            name='rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='hotplace',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='CONTENT'),
        ),
    ]

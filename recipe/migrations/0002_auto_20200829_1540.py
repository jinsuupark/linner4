# Generated by Django 3.1 on 2020-08-29 15:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reply',
            name='Rep_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='reply',
            name='Rep_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_member', to=settings.AUTH_USER_MODEL),
        ),
    ]
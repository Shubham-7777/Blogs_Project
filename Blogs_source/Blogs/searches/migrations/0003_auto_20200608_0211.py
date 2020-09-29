# Generated by Django 3.0.2 on 2020-06-07 20:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('searches', '0002_auto_20200608_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search_model',
            name='user',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]

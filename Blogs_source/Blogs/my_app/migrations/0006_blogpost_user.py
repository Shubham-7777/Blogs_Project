# Generated by Django 3.0.2 on 2020-05-30 15:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_app', '0005_auto_20200530_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]

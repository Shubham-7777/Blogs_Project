# Generated by Django 3.0.2 on 2020-06-07 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0013_auto_20200607_2224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', '-updated', '-timestamp']},
        ),
    ]

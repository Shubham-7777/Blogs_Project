# Generated by Django 3.0.2 on 2020-06-03 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_auto_20200603_1913'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['publish_date', '-updated', 'timestamp']},
        ),
    ]

# Generated by Django 4.0.2 on 2022-02-24 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='update',
        ),
    ]

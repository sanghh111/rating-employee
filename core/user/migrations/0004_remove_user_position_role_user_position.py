# Generated by Django 4.0 on 2022-05-22 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_created_at_user_created_by_user_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='position_role',
        ),
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

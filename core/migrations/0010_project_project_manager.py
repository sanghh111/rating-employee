# Generated by Django 4.0 on 2022-05-23 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_remove_user_position_role_user_position'),
        ('core', '0009_lograting_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]

# Generated by Django 4.0 on 2022-05-19 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_userpermission_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectuserwork',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_id', to='core.project'),
        ),
    ]

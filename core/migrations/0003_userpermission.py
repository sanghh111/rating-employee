# Generated by Django 4.0 on 2022-05-18 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('user', '0003_user_created_at_user_created_by_user_updated_at_and_more'),
        ('core', '0002_userrolepermission_detailrating_project_role_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', null=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='modified_at', null=True, verbose_name='Updated at')),
                ('created_by', models.CharField(blank=True, db_column='created_by', default='', max_length=100, null=True, verbose_name='Created by')),
                ('updated_by', models.CharField(blank=True, db_column='modified_by', default='', max_length=100, null=True, verbose_name='Updated by')),
                ('permission_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.permission')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'user_permission',
            },
        ),
    ]

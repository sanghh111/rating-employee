# Generated by Django 4.0 on 2022-03-21 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_userrolepermission_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='TempUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'TempUser',
                'managed': False,
            },
        ),
    ]

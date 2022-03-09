# Generated by Django 4.0.2 on 2022-03-09 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='position',
        ),
        migrations.AddField(
            model_name='user',
            name='account_token_reset_pass',
            field=models.CharField(blank=True, db_column='account_token_reset_pass', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='account_token_reset_pass_time',
            field=models.DateTimeField(blank=True, db_column='account_token_reset_pass_time', null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='position_role',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, db_column='account_token', max_length=200, null=True, verbose_name='Token'),
        ),
        migrations.AddField(
            model_name='user',
            name='token_date',
            field=models.DateField(blank=True, db_column='account_token_date', null=True, verbose_name='Token Date'),
        ),
    ]

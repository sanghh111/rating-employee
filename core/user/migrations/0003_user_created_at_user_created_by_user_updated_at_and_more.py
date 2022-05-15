# Generated by Django 4.0 on 2022-03-23 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_user_position_user_account_token_reset_pass_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_column='created_at', null=True, verbose_name='Created at'),
        ),
        migrations.AddField(
            model_name='user',
            name='created_by',
            field=models.CharField(blank=True, db_column='created_by', default='', max_length=100, null=True, verbose_name='Created by'),
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, db_column='modified_at', null=True, verbose_name='Updated at'),
        ),
        migrations.AddField(
            model_name='user',
            name='updated_by',
            field=models.CharField(blank=True, db_column='modified_by', default='', max_length=100, null=True, verbose_name='Updated by'),
        ),
    ]
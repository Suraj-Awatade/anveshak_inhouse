# Generated by Django 4.0.8 on 2022-10-14 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_account_managers_alter_account_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='password_reset',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
# Generated by Django 4.1.2 on 2022-10-31 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0023_alter_account_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_staff',
            field=models.BooleanField(default=1),
        ),
    ]
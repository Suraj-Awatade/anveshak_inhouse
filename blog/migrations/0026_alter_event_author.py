# Generated by Django 4.1.2 on 2022-10-31 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_event_account_alter_event_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='author',
            field=models.CharField(max_length=255),
        ),
    ]
# Generated by Django 4.1.2 on 2022-10-20 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_event_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
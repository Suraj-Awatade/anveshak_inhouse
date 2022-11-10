# Generated by Django 4.1.2 on 2022-10-27 04:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0013_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='account',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to=settings.AUTH_USER_MODEL),
        ),
    ]
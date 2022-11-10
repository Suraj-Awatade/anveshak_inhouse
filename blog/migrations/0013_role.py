# Generated by Django 4.1.2 on 2022-10-26 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_alter_event_title_rename_title_event_title_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField(default=0)),
                ('is_reviewer', models.BooleanField(default=0)),
                ('is_content_writer', models.BooleanField(default=0)),
                ('is_author', models.BooleanField(default=0)),
                ('is_user', models.BooleanField(default=1)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Role',
            },
        ),
    ]
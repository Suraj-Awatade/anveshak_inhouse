# Generated by Django 4.1.2 on 2022-10-29 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_role_is_admin_alter_role_is_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewcomment',
            name='added_by',
        ),
        migrations.RemoveField(
            model_name='reviewcomment',
            name='reviewer_status',
        ),
    ]

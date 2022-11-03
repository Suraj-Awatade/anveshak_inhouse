# Generated by Django 4.1.2 on 2022-10-31 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_alter_event_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('A', 'Approved'), ('R', 'Rejected'), ('U', 'Under Review'), ('S', 'Submitted'), ('RS', 'Resubmitted'), ('RW', 'Rework')], default='U', max_length=12),
        ),
    ]

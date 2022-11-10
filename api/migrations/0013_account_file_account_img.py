# Generated by Django 4.1.2 on 2022-10-17 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_document_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='file',
            field=models.FileField(default='Docs/None/No-doc.pdf', upload_to='Docs/'),
        ),
        migrations.AddField(
            model_name='account',
            name='img',
            field=models.ImageField(default='Images/None/No-img.jpg', upload_to='Images/'),
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-17 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_rename_user_document_account_document_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(default='Docs/None/No-doc.txt', upload_to='Docs/'),
        ),
        migrations.AlterField(
            model_name='document',
            name='img',
            field=models.ImageField(default='Images/None/No-img.jpg', upload_to='Images/'),
        ),
    ]
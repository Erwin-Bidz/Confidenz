# Generated by Django 4.2.1 on 2023-06-14 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basefinale', '0009_fichier_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fichier',
            options={'ordering': ['-upload_date']},
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-14 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basefinale', '0007_employe_identifier_alter_employe_matricule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fichier',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]

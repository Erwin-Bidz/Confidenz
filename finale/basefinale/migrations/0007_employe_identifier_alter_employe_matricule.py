# Generated by Django 4.2.1 on 2023-05-30 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basefinale', '0006_fichier_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='employe',
            name='identifier',
            field=models.CharField(default=1, max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employe',
            name='matricule',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

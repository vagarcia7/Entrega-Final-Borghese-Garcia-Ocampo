# Generated by Django 4.0 on 2022-01-29 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_post'),
        ),
    ]

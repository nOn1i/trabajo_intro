# Generated by Django 4.2.4 on 2023-10-18 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pruebas', '0003_remove_profile_image_profile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
# Generated by Django 3.2.8 on 2021-11-11 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstService', '0006_profile_image_converted'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image_result',
            field=models.ImageField(null=True, upload_to='imagesResult/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]

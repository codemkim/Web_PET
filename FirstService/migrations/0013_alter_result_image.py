# Generated by Django 3.2.8 on 2021-11-23 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstService', '0012_alter_result_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='image',
            field=models.ImageField(null=True, upload_to='imagesResult/'),
        ),
    ]

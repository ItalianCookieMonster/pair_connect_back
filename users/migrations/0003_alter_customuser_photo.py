# Generated by Django 5.1.1 on 2024-09-27 09:30

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_managers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='photo',
            field=cloudinary.models.CloudinaryField(blank=True, default='https://res.cloudinary.com/dwzqcmaod/image/upload/v1727428844/default_avatar_pew52f.jpg', max_length=255, null=True, verbose_name='image'),
        ),
    ]

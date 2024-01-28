# Generated by Django 4.2 on 2024-01-26 20:52

from django.db import migrations, models
import userauths.models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0004_alter_profile_cover_image_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cover_image',
            field=models.ImageField(blank=True, default='cover.jpg', null=True, upload_to=userauths.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=userauths.models.user_directory_path),
        ),
    ]
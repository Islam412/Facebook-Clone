# Generated by Django 4.2 on 2024-02-15 01:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields
import userauths.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_alter_notification_comment_alter_notification_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=userauths.models.user_directory_path)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to=userauths.models.user_directory_path)),
                ('visibility', models.CharField(choices=[('Only Me', 'Only Me'), ('Everyone', 'Everyone')], default='Everyone', max_length=100)),
                ('gid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxyz1234567890', length=7, max_length=25, prefix='')),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(unique=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('memebers', models.ManyToManyField(related_name='group_memebers', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=userauths.models.user_directory_path)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to=userauths.models.user_directory_path)),
                ('visibility', models.CharField(choices=[('Only Me', 'Only Me'), ('Everyone', 'Everyone')], default='Everyone', max_length=100)),
                ('pid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxyz1234567890', length=7, max_length=25, prefix='')),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(unique=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('followers', models.ManyToManyField(related_name='page_memebers', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='page_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PagePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=userauths.models.user_directory_path)),
                ('video', models.FileField(blank=True, null=True, upload_to=userauths.models.user_directory_path)),
                ('visibility', models.CharField(choices=[('Only Me', 'Only Me'), ('Everyone', 'Everyone')], default='Everyone', max_length=100)),
                ('pid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxyz1234567890', length=7, max_length=25, prefix='')),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(unique=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='page_post_likes', to=settings.AUTH_USER_MODEL)),
                ('page', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.page')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GroupPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=userauths.models.user_directory_path)),
                ('video', models.FileField(blank=True, null=True, upload_to=userauths.models.user_directory_path)),
                ('visibility', models.CharField(choices=[('Only Me', 'Only Me'), ('Everyone', 'Everyone')], default='Everyone', max_length=100)),
                ('pid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxyz1234567890', length=7, max_length=25, prefix='')),
                ('active', models.BooleanField(default=True)),
                ('slug', models.SlugField(unique=True)),
                ('views', models.PositiveIntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.group')),
                ('likes', models.ManyToManyField(blank=True, related_name='group_post_likes', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

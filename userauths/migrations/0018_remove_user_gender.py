# Generated by Django 4.2 on 2024-02-08 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0017_alter_user_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
    ]

# Generated by Django 4.2 on 2024-02-09 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0018_remove_user_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_name',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
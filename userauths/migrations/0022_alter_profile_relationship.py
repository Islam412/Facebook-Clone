# Generated by Django 4.2 on 2024-04-23 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0021_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='relationship',
            field=models.CharField(blank=True, choices=[('single', 'Single'), ('married', 'married'), ('Egaged', 'Egaged')], max_length=100, null=True),
        ),
    ]

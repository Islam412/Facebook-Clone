# Generated by Django 4.2 on 2024-04-17 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0010_alter_chatmessage_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatmessage',
            options={'verbose_name_plural': 'ChatMessages'},
        ),
        migrations.RemoveField(
            model_name='chatmessage',
            name='reciever',
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chat_receiver', related_query_name='chat_receiver', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='chat_sender', related_query_name='chat_sender', to=settings.AUTH_USER_MODEL),
        ),
    ]

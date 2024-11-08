# Generated by Django 5.1.1 on 2024-10-25 14:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_remove_notification_user_delete_friendrequest_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_relationships', to=settings.AUTH_USER_MODEL)),
                ('friends', models.ManyToManyField(related_name='friends_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

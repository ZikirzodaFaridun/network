# Generated by Django 5.1.1 on 2024-11-04 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0046_remove_textpost_likes_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='textpost',
            name='likes_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

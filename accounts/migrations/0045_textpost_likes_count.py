# Generated by Django 5.1.1 on 2024-11-04 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0044_textpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='textpost',
            name='likes_count',
            field=models.IntegerField(default=0),
        ),
    ]

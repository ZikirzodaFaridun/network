# Generated by Django 5.1.1 on 2024-11-07 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0056_post_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes_count',
            field=models.IntegerField(default=0),
        ),
    ]

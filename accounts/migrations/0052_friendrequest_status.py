# Generated by Django 5.1.1 on 2024-11-06 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0051_rename_timestamp_friendrequest_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendrequest',
            name='status',
            field=models.CharField(choices=[('sent', 'Sent'), ('accepted', 'Accepted'), ('declined', 'Declined')], default='sent', max_length=10),
        ),
    ]

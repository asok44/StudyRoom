# Generated by Django 3.2.7 on 2023-08-13 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_room_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-14 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exchange', '0003_bookrequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookrequest',
            name='message',
        ),
    ]

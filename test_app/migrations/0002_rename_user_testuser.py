# Generated by Django 4.2.16 on 2024-10-18 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='TestUser',
        ),
    ]

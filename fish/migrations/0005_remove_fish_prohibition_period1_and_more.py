# Generated by Django 4.1 on 2023-02-14 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fish', '0004_alter_fish_is_deleted_alter_fish_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fish',
            name='prohibition_period1',
        ),
        migrations.RemoveField(
            model_name='fish',
            name='prohibition_period2',
        ),
    ]

# Generated by Django 4.1 on 2023-02-27 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fish', '0006_alter_fishimage_is_deleted_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fish',
            old_name='end_date',
            new_name='end_date2',
        ),
        migrations.RenameField(
            model_name='fish',
            old_name='start_date',
            new_name='start_date2',
        ),
    ]
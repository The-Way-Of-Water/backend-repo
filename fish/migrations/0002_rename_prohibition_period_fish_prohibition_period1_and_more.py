# Generated by Django 4.1 on 2023-02-14 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fish', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fish',
            old_name='prohibition_period',
            new_name='prohibition_period1',
        ),
        migrations.AddField(
            model_name='fish',
            name='prohibition_period2',
            field=models.CharField(max_length=225, null=True),
        ),
    ]

# Generated by Django 3.0.6 on 2021-09-19 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mybank', '0002_auto_20210816_1817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transfer',
            old_name='fromano',
            new_name='fromAccNo',
        ),
        migrations.RenameField(
            model_name='transfer',
            old_name='toano',
            new_name='toAccNo',
        ),
    ]

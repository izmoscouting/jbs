# Generated by Django 4.2.6 on 2024-01-24 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wasserman_core', '0015_rename_id_player_unique_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='unique_id',
            new_name='id',
        ),
    ]

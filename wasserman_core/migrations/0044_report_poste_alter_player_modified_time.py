# Generated by Django 4.2.6 on 2024-02-29 23:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wasserman_core', '0043_remove_player_agent_player_contact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='poste',
            field=models.CharField(default='-', max_length=500),
        ),
        migrations.AlterField(
            model_name='player',
            name='modified_time',
            field=models.DateField(default=datetime.datetime.today),
        ),
    ]

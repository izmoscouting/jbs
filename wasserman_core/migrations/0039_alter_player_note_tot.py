# Generated by Django 4.2.6 on 2024-01-26 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wasserman_core', '0038_alter_player_note_actuel_alter_player_note_financ_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='note_tot',
            field=models.CharField(default='R0', editable=False, max_length=5),
        ),
    ]

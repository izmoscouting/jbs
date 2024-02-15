# Generated by Django 4.2.6 on 2024-01-24 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wasserman_core', '0005_agency_statut_remove_scout_agent_player_agent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Situation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Situation', models.CharField(max_length=500)),
            ],
        ),
        migrations.DeleteModel(
            name='Statut',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='date',
            new_name='date_prop',
        ),
        migrations.RemoveField(
            model_name='player',
            name='email',
        ),
        migrations.RemoveField(
            model_name='player',
            name='transferable',
        ),
        migrations.AddField(
            model_name='player',
            name='champ',
            field=models.CharField(default='-', max_length=500),
        ),
        migrations.AddField(
            model_name='player',
            name='comment',
            field=models.CharField(default='-', max_length=2000),
        ),
        migrations.AddField(
            model_name='player',
            name='end_contract',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='player',
            name='end_mand',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='player',
            name='move_cond',
            field=models.CharField(default='-', max_length=500),
        ),
        migrations.AddField(
            model_name='player',
            name='note',
            field=models.CharField(default='R1', max_length=5),
        ),
        migrations.AddField(
            model_name='player',
            name='release',
            field=models.CharField(default='-', max_length=500),
        ),
        migrations.AddField(
            model_name='player',
            name='system',
            field=models.CharField(default='4-4-2', max_length=500),
        ),
        migrations.AlterField(
            model_name='player',
            name='club',
            field=models.CharField(default='FCA', max_length=500),
        ),
        migrations.AlterField(
            model_name='player',
            name='foot',
            field=models.CharField(default='-', max_length=500),
        ),
        migrations.AlterField(
            model_name='player',
            name='other_pos',
            field=models.CharField(default='-', max_length=500),
        ),
        migrations.AlterField(
            model_name='player',
            name='phone',
            field=models.CharField(default=612456789, max_length=10000),
        ),
        migrations.AlterField(
            model_name='player',
            name='potential',
            field=models.CharField(default='R1', max_length=10),
        ),
        migrations.AlterField(
            model_name='player',
            name='wage',
            field=models.CharField(default=1200, max_length=100),
        ),
        migrations.AddField(
            model_name='player',
            name='situation',
            field=models.ManyToManyField(to='wasserman_core.situation'),
        ),
    ]

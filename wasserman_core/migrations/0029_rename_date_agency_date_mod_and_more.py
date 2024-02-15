# Generated by Django 4.2.6 on 2024-01-25 22:42

import datetime
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wasserman_core', '0028_remove_player_agency_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agency',
            old_name='date',
            new_name='date_mod',
        ),
        migrations.RenameField(
            model_name='business',
            old_name='date',
            new_name='mod_time',
        ),
        migrations.RenameField(
            model_name='club',
            old_name='note_totale',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='coach',
            old_name='actual',
            new_name='rating',
        ),
        migrations.RemoveField(
            model_name='agency',
            name='email',
        ),
        migrations.RemoveField(
            model_name='agency',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='agency',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='agency',
            name='password',
        ),
        migrations.RemoveField(
            model_name='agency',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='agency',
            name='photo',
        ),
        migrations.AddField(
            model_name='agency',
            name='city',
            field=models.CharField(default='Inconnu', max_length=150),
        ),
        migrations.AddField(
            model_name='agency',
            name='country',
            field=models.CharField(default='Inconnu', max_length=150),
        ),
        migrations.AddField(
            model_name='agency',
            name='date_crea',
            field=models.CharField(default=django.contrib.auth.models.User, editable=False, max_length=150),
        ),
        migrations.AddField(
            model_name='agency',
            name='name',
            field=models.CharField(default='Inconnu', max_length=225),
        ),
        migrations.AddField(
            model_name='agency',
            name='notes',
            field=models.CharField(default='Inconnu', max_length=2000),
        ),
        migrations.AddField(
            model_name='agency',
            name='web',
            field=models.CharField(default='Inconnu', max_length=150),
        ),
        migrations.AddField(
            model_name='business',
            name='closing_date',
            field=models.DateField(default=datetime.datetime(9999, 12, 31, 0, 0)),
        ),
        migrations.AddField(
            model_name='business',
            name='club_id',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='wasserman_core.club'),
        ),
        migrations.AddField(
            model_name='business',
            name='created_by',
            field=models.CharField(default=django.contrib.auth.models.User, editable=False, max_length=150),
        ),
        migrations.AddField(
            model_name='business',
            name='date_created',
            field=models.DateField(default=datetime.datetime.today, editable=False),
        ),
        migrations.AddField(
            model_name='business',
            name='desc',
            field=models.CharField(default='-', max_length=250),
        ),
        migrations.AddField(
            model_name='business',
            name='lead_source',
            field=models.CharField(default='Partenaire', max_length=50),
        ),
        migrations.AddField(
            model_name='business',
            name='next_step',
            field=models.CharField(default='Attente', max_length=225),
        ),
        migrations.AddField(
            model_name='business',
            name='pos_voulu',
            field=models.CharField(default='Inconnu', max_length=150),
        ),
        migrations.AddField(
            model_name='business',
            name='rea_for_loss',
            field=models.CharField(default='-', max_length=250),
        ),
        migrations.AddField(
            model_name='business',
            name='stage',
            field=models.CharField(default='Inconnu', max_length=225),
        ),
        migrations.AddField(
            model_name='club',
            name='club_type',
            field=models.CharField(default='Inconnu', max_length=150),
        ),
        migrations.AddField(
            model_name='club',
            name='commentaires',
            field=models.CharField(default='-', max_length=2000),
        ),
        migrations.AddField(
            model_name='club',
            name='created_by',
            field=models.CharField(default=django.contrib.auth.models.User, editable=False, max_length=150),
        ),
        migrations.AddField(
            model_name='club',
            name='industry',
            field=models.CharField(default='Inconnu', max_length=150),
        ),
        migrations.AddField(
            model_name='club',
            name='mod_by',
            field=models.CharField(default=django.contrib.auth.models.User, editable=False, max_length=150),
        ),
        migrations.AddField(
            model_name='club',
            name='ownership',
            field=models.CharField(default='Inconnu', max_length=150),
        ),
        migrations.AddField(
            model_name='club',
            name='parent_club',
            field=models.CharField(default='Aucun', max_length=150),
        ),
        migrations.AddField(
            model_name='coach',
            name='created_by',
            field=models.CharField(default=django.contrib.auth.models.User, editable=False, max_length=150),
        ),
        migrations.AddField(
            model_name='player',
            name='agence_id',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='wasserman_core.agency'),
        ),
        migrations.AddField(
            model_name='player',
            name='created_by',
            field=models.CharField(default=django.contrib.auth.models.User, editable=False, max_length=150),
        ),
        migrations.AlterField(
            model_name='business',
            name='name',
            field=models.CharField(default='Inconnu', max_length=150),
        ),
        migrations.AlterField(
            model_name='player',
            name='birth',
            field=models.DateField(default=datetime.datetime(1899, 12, 31, 0, 0)),
        ),
        migrations.AlterField(
            model_name='player',
            name='created_time',
            field=models.DateField(default=datetime.datetime.today, editable=False),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(default='Inconnu', max_length=50)),
                ('last_name', models.CharField(default='Inconnu', max_length=50)),
                ('name', models.CharField(default='Inconnu', max_length=50)),
                ('phone', models.CharField(default='Inconnu', max_length=50)),
                ('email', models.EmailField(default='Inconnu', max_length=100)),
                ('phone_2', models.CharField(default='-', max_length=150)),
                ('commentaires', models.CharField(default='-', max_length=1500)),
                ('created_by', models.CharField(default=django.contrib.auth.models.User, editable=False, max_length=150)),
                ('mod_by', models.CharField(default=django.contrib.auth.models.User, editable=False, max_length=150)),
                ('date_crea', models.DateField(default=datetime.datetime.today, editable=False)),
                ('club_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wasserman_core.club')),
            ],
        ),
        migrations.AddField(
            model_name='agency',
            name='contact_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wasserman_core.contact'),
        ),
        migrations.AddField(
            model_name='business',
            name='contact_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wasserman_core.contact'),
        ),
    ]
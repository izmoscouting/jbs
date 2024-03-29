# Generated by Django 4.2.6 on 2024-01-25 23:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wasserman_core', '0033_agency_crea_by_agency_mod_by_alter_agency_date_crea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='club_id',
            field=models.ForeignKey(default=uuid.uuid4, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wasserman_core.club'),
        ),
        migrations.AlterField(
            model_name='player',
            name='agence_id',
            field=models.ForeignKey(default=uuid.uuid4, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wasserman_core.agency'),
        ),
        migrations.AlterField(
            model_name='player',
            name='club_id',
            field=models.ForeignKey(default=uuid.uuid4, null=True, on_delete=django.db.models.deletion.SET_NULL, to='wasserman_core.club'),
        ),
    ]

# Generated by Django 4.2.6 on 2024-01-25 18:26

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wasserman_core', '0026_rename_ide_club_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='club_id',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='wasserman_core.club'),
        ),
    ]
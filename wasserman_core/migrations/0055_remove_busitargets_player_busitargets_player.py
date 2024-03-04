# Generated by Django 4.2.6 on 2024-03-04 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wasserman_core', '0054_busitargets_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='busitargets',
            name='player',
        ),
        migrations.AddField(
            model_name='busitargets',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wasserman_core.player'),
        ),
    ]
# Generated by Django 4.2.6 on 2024-01-24 17:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('wasserman_core', '0012_alter_player_foot'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUUIDModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='player',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
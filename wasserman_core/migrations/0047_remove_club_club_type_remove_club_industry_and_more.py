# Generated by Django 4.2.6 on 2024-03-01 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wasserman_core', '0046_alter_club_coach_infomercato'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='club',
            name='club_type',
        ),
        migrations.RemoveField(
            model_name='club',
            name='industry',
        ),
        migrations.RemoveField(
            model_name='club',
            name='ownership',
        ),
        migrations.AlterField(
            model_name='agency',
            name='crea_by',
            field=models.CharField(max_length=150, null=True),
        ),
    ]

# Generated by Django 4.2.6 on 2024-01-26 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wasserman_core', '0037_alter_club_actual_alter_club_financial_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='note_actuel',
            field=models.CharField(default='R0', max_length=10),
        ),
        migrations.AlterField(
            model_name='player',
            name='note_financ',
            field=models.CharField(default='R0', max_length=10),
        ),
        migrations.AlterField(
            model_name='player',
            name='note_tot',
            field=models.CharField(default='R0', max_length=5),
        ),
        migrations.AlterField(
            model_name='player',
            name='potential',
            field=models.CharField(default='R0', max_length=10),
        ),
    ]

# Generated by Django 4.1.4 on 2023-07-04 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_end_time_alter_event_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(),
        ),
    ]

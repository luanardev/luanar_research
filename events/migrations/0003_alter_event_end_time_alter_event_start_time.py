# Generated by Django 4.1.4 on 2023-07-04 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_event_created_at_event_end_time_event_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.TimeField(auto_now_add=True, null=True),
        ),
    ]
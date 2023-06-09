# Generated by Django 4.1.5 on 2023-02-23 09:02

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Innovation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('patent', models.CharField(max_length=255)),
                ('year_of_innovation', models.IntegerField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Innovator',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('innovation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='innovation.innovation')),
            ],
        ),
        migrations.CreateModel(
            name='InnovationMedia',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('media', models.FileField(blank=True, upload_to='innovation_media/%Y/%m/%d/')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('innovation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='innovation.innovation')),
            ],
        ),
    ]

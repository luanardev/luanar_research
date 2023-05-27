# Generated by Django 4.1.4 on 2023-03-29 07:04

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('co_authors', models.TextField(blank=True, null=True)),
                ('title', models.CharField(max_length=255)),
                ('abstract', models.TextField()),
                ('journal_name', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('publication_type', models.CharField(max_length=255)),
                ('year_of_publication', models.IntegerField()),
                ('number_of_pages', models.CharField(blank=True, max_length=255, null=True)),
                ('volume', models.IntegerField(blank=True, null=True)),
                ('license', models.CharField(max_length=255)),
                ('collection', models.CharField(max_length=255)),
                ('doi', models.CharField(max_length=255, unique=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
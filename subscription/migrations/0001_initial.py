# Generated by Django 4.1.4 on 2023-03-23 20:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
            ],
        ),
    ]
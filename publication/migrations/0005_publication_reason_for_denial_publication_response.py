# Generated by Django 4.1.4 on 2023-06-29 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0004_alter_publication_doi'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='reason_for_denial',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='response',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.1.4 on 2023-07-01 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_remove_member_role_remove_project_donor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='reason_for_denial',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='response',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]

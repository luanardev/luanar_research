# Generated by Django 4.1.4 on 2023-06-15 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_remove_member_role_remove_project_donor_and_more'),
        ('publication', '0002_publication_image_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='project.project'),
        ),
    ]

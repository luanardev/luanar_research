# Generated by Django 4.1.4 on 2023-06-09 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='role',
        ),
        migrations.RemoveField(
            model_name='project',
            name='donor',
        ),
        migrations.RemoveField(
            model_name='project',
            name='file_name',
        ),
        migrations.RemoveField(
            model_name='project',
            name='member',
        ),
        migrations.RemoveField(
            model_name='project',
            name='partner',
        ),
        migrations.AddField(
            model_name='project',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='date_from',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='expected_completion_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='image_path',
            field=models.ImageField(blank=True, null=True, upload_to='projects/'),
        ),
        migrations.AddField(
            model_name='project',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='project_co_pi',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_donor',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_member',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_partner',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_pi',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='supporting_document',
            field=models.FileField(blank=True, null=True, upload_to='project_documents/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='project',
            name='total_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Donor',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.DeleteModel(
            name='Partner',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]

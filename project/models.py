from django.db import models
from datetime import datetime
from django.db.models import DO_NOTHING
import uuid
from account.models import User

# Create your models here.
class Project(models.Model):
    id            = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user          = models.ForeignKey(User, on_delete=DO_NOTHING,blank=True, null=True)
    title         = models.CharField(max_length=255)
    total_value    = models.FloatField(blank=True, null=True)
    project_status = models.CharField(max_length=255,blank=True, null=True)
    project_type   = models.CharField(max_length=255,blank=True, null=True)
    project_pi = models.CharField(max_length=255,blank=True, null=True)
    project_co_pi = models.CharField(max_length=255,blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    expected_completion_date = models.DateField(blank=True, null=True)
    project_member = models.TextField(blank=True, null=True)
    project_donor = models.TextField(blank=True, null=True)
    project_partner = models.TextField(blank=True, null=True)
    description = models.TextField()
    supporting_document = models.FileField(upload_to='project_documents/%Y/%m/%d/', blank=True, null=True)
    image_path = models.ImageField(upload_to='projects/', blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now)
    is_approved = models.BooleanField(default=False)
    response = models.BooleanField(blank=True,null=True)
    reason_for_denial = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}"
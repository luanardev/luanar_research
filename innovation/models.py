from django.db import models
from django.db.models import DO_NOTHING
from datetime import datetime
import uuid
from account.models import User

# Create your models here.

    
class Innovation(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    title = models.CharField(max_length=255)
    description = models.TextField()
    patent = models.CharField(max_length=255)
    year_of_innovation = models.IntegerField()
    media = models.FileField(upload_to='innovation_media/%Y/%m/%d/', blank=True, null=True)
    youtube_code = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(
        default=datetime.now)
    
    def __str__(self):
        return f"{self.title}"

    # def media(self):
    #     return InnovationMedia.objects.filter(innovation = self.id)
    
    def innovators(self):
        return Innovator.objects.filter(innovation = self.id)

# class InnovationMedia(models.Model):
#     id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
#     innovation = models.ForeignKey(Innovation, on_delete=DO_NOTHING)
#     media = models.FileField(upload_to='innovation_media/%Y/%m/%d/', blank=True)
#     description = models.TextField()
#     created_at = models.DateTimeField(
#         default=datetime.now)

#     def __str__(self):
#         return f"{self.innovation}"
    
class Innovator(models.Model):
    id = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    innovation = models.ForeignKey(Innovation, on_delete=DO_NOTHING)
    title = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(
        default=datetime.now)
    
    def __str__(self):
        return f"{self.title} {self.first_name} {self.last_name}"
    
    def name(self):
        return f"{self.title} {self.first_name} {self.last_name}"


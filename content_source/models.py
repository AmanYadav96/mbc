from django.db import models
import uuid
# Create your models here.
from django.db import models
from content.models import Content

class Source(models.Model):
    source_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    content_id = models.ForeignKey(Content , on_delete=models.CASCADE , default=uuid.uuid4)
    content_type = models.CharField(max_length=100)
    source_title = models.CharField(max_length=255)
    source_quality = models.CharField(max_length=100)
    source_size = models.CharField(max_length=100)
    downloadable = models.BooleanField(default=False)
    access_type = models.CharField(max_length=100)
    source_type = models.CharField(max_length=100)
    source = models.URLField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.source_title

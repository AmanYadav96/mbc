from django.db import models
import uuid
from content.models import Content
from content_season.models import Season

# Create your models here.
class Episodes(models.Model):
    episode_id = models.UUIDField(primary_key=True)
    season_id = models.ForeignKey(Season , on_delete=models.CASCADE , default=uuid.uuid4)
    content_id = models.ForeignKey(Content, on_delete=models.CASCADE, default=uuid.uuid4)
    episode_title = models.CharField(max_length=999)
    episode_number = models.PositiveIntegerField()
    source_quality = models.CharField(max_length=999)
    source_size = models.CharField(max_length=999)
    downloadable = models.BooleanField(default=False)
    access_type = models.CharField(max_length=999)
    episode_source_type = models.CharField(max_length=999)
    source = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
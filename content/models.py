from django.db import models
import uuid
from networks.models import Network
# Create your models here.
class Content(models.Model):
    content_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    network = models.ForeignKey(Network, on_delete=models.CASCADE, default=uuid.uuid4)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    content_type = models.CharField(max_length= 999)
    duration = models.TimeField(blank=True)
    release_year = models.DateField(blank=True)
    ratings = models.FloatField()
    language = models.CharField(max_length=999)
    trailer_url = models.URLField(blank=True)
    verticle_poster = models.ImageField(upload_to='verticle-poster',blank=True)
    horizontol_poster = models.ImageField(upload_to='horizontol-poster',blank=True,null=True)
    slider = models.BooleanField(default=False)
    genre = models.CharField(max_length=999)
    is_featured = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
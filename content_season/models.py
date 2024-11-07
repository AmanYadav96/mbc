from django.db import models
import uuid
from content.models import Content
# Create your models here.
class Season(models.Model):
    season_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    content = models.ForeignKey(Content, on_delete=models.CASCADE)
    title = models.CharField(max_length=999)
    trailer = models.FileField(upload_to='Season-trailer',blank = True , null=True)
    image = models.ImageField(upload_to='Season-image')
    is_trending = models.BooleanField(default=False)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
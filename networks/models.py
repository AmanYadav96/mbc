from django.db import models

# Create your models here.
from django.db import models
import uuid
# Create your models here.
class Network(models.Model):
    network_id = models.UUIDField(primary_key=True, default= uuid.uuid4)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    network_image = models.ImageField(upload_to='network_image',blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
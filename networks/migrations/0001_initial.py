# Generated by Django 5.1.1 on 2024-11-05 20:23

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Network",
            fields=[
                (
                    "network_id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True)),
                ("network_image", models.ImageField(upload_to="network-image")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
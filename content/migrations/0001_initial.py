# Generated by Django 5.1.1 on 2024-11-05 20:23

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("networks", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Content",
            fields=[
                (
                    "content_id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True)),
                ("content_type", models.CharField(max_length=999)),
                ("duration", models.TimeField(blank=True)),
                ("release_year", models.DateField(blank=True)),
                ("ratings", models.FloatField()),
                ("language", models.CharField(max_length=999)),
                ("trailer_url", models.URLField(blank=True)),
                ("verticle_poster", models.ImageField(upload_to="verticle_poster")),
                ("Horizontol_poster", models.ImageField(upload_to="horizontol_poster")),
                ("genre", models.CharField(max_length=999)),
                ("is_featured", models.BooleanField(default=False)),
                ("is_trending", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "network",
                    models.ForeignKey(
                        default=uuid.uuid4,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="networks.network",
                    ),
                ),
            ],
        ),
    ]
# Generated by Django 5.1.1 on 2024-11-05 20:23

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("content", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Season",
            fields=[
                (
                    "season_id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("title", models.CharField(max_length=999)),
                ("trailer", models.FileField(upload_to="season-trailer")),
                ("image", models.ImageField(upload_to="season-image")),
                ("description", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "content",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="content.content",
                    ),
                ),
            ],
        ),
    ]
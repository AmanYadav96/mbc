# Generated by Django 5.1.1 on 2024-11-06 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("networks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="network",
            name="network_image",
            field=models.URLField(blank=True),
        ),
    ]
# Generated by Django 5.1.1 on 2024-11-07 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("networks", "0006_alter_network_network_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="network",
            name="network_image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
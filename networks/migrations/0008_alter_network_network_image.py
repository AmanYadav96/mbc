# Generated by Django 5.1.1 on 2024-11-11 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("networks", "0007_alter_network_network_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="network",
            name="network_image",
            field=models.ImageField(blank=True, null=True, upload_to="network_image"),
        ),
    ]

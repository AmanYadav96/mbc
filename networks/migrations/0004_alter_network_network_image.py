# Generated by Django 5.1.1 on 2024-11-06 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("networks", "0003_alter_network_network_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="network",
            name="network_image",
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-15 03:23

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):
    dependencies = [
        ("traffic", "0005_remove_trafficguidancescheme_road_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="TrafficRequiredArrangement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "map_pin",
                    django.contrib.gis.db.models.fields.PointField(
                        blank=True, null=True, srid=4326
                    ),
                ),
                ("date_of_installation", models.DateField(blank=True, null=True)),
                (
                    "traffic",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="traffic_required_arrangements",
                        to="traffic.traffic",
                    ),
                ),
                (
                    "traffic_guidance_scheme",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="traffic_required_arrangements",
                        to="traffic.trafficguidancescheme",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Traffic Required Arrangements",
            },
        ),
    ]
# Generated by Django 4.2.7 on 2023-11-30 07:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "prescriptiondetails",
            "0006_remove_fueltype_applicable_fuel_type_prescription_details_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="ApplicableFuelTypePrescriptionDetail",
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
                    "prescription_detail",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("scorch_height", "Scorch Height"),
                            ("burn_area", "Area to be burnt"),
                            ("ros_range", "Rate of Spread"),
                            ("ffdi_range", "Forest Fire Danger Index"),
                            ("glc_range", "Ground Level Concentration"),
                            ("gfdi_range", "Grass Fire Danger Index"),
                            ("temperature_range", "Temperature"),
                            ("rh_range", "Relative Humidity"),
                            ("sdi", "Soil Dryness Index"),
                            ("smc_range", "Surface Fuel Moisture Content"),
                            ("pmc_range", "Profile Fuel Moisture Content"),
                            ("wind_speed_range", "Wind Speed"),
                            ("wind_direction", "Wind Direction"),
                        ],
                        max_length=255,
                        null=True,
                        unique=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Applicable Fuel Type Prescription Detail",
                "verbose_name_plural": "Applicable Fuel Type Prescription Details",
            },
        ),
        migrations.AddField(
            model_name="fueltype",
            name="applicable_fuel_type_prescription_details",
            field=models.ManyToManyField(
                related_name="fuel_types",
                to="prescriptiondetails.applicablefueltypeprescriptiondetail",
            ),
        ),
    ]

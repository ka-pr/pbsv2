# Generated by Django 4.2.7 on 2023-11-29 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        (
            "prescriptiondetails",
            "0002_burnarea_ffdirange_gfdirange_glcrange_pmcrange_and_more",
        ),
        ("operationalplanning", "0054_prescriptionfueltype_prescription_fuel_types"),
    ]

    operations = [
        migrations.AddField(
            model_name="prescriptionfueltype",
            name="burn_area",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="prescription_fuel_types",
                to="prescriptiondetails.burnarea",
                verbose_name="Area to be burnt",
            ),
        ),
        migrations.AddField(
            model_name="prescriptionfueltype",
            name="cell_name",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Cell"
            ),
        ),
        migrations.AddField(
            model_name="prescriptionfueltype",
            name="ffdi_range",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="prescription_fuel_types",
                to="prescriptiondetails.ffdirange",
                verbose_name="Forest Fire Danger Index (FFDI)",
            ),
        ),
        migrations.AddField(
            model_name="prescriptionfueltype",
            name="gfdi_range",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="prescription_fuel_types",
                to="prescriptiondetails.gfdirange",
                verbose_name="Grass Fire Danger Index (GFDI)",
            ),
        ),
        migrations.AddField(
            model_name="prescriptionfueltype",
            name="glc_range",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="prescription_fuel_types",
                to="prescriptiondetails.glcrange",
                verbose_name="Ground Level Concentration??? (GLC)",
            ),
        ),
        migrations.AddField(
            model_name="prescriptionfueltype",
            name="pmc_range",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="prescription_fuel_types",
                to="prescriptiondetails.pmcrange",
                verbose_name="Profile Moisture Content (PMC)",
            ),
        ),
        migrations.AddField(
            model_name="prescriptionfueltype",
            name="rh_range",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="prescription_fuel_types",
                to="prescriptiondetails.rhrange",
                verbose_name="Relative Humidity (RH)",
            ),
        ),
        migrations.AddField(
            model_name="prescriptionfueltype",
            name="ros_range",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="prescription_fuel_types",
                to="prescriptiondetails.rosrange",
                verbose_name="Rate of Spread (ROS)",
            ),
        ),
        migrations.AddField(
            model_name="prescriptionfueltype",
            name="scorch_height",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="prescription_fuel_types",
                to="prescriptiondetails.scorchheight",
                verbose_name="Scorch Height",
            ),
        ),
        migrations.AddField(
            model_name="prescriptionfueltype",
            name="sdi",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="prescription_fuel_types",
                to="prescriptiondetails.sdi",
                verbose_name="Soil Dryness Index (SDI)",
            ),
        ),
        migrations.AddField(
            model_name="prescriptionfueltype",
            name="smc_range",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="prescription_fuel_types",
                to="prescriptiondetails.smcrange",
                verbose_name="Soil Moisture Content (SMC)",
            ),
        ),
        migrations.AddField(
            model_name="prescriptionfueltype",
            name="temperature_range",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="prescription_fuel_types",
                to="prescriptiondetails.temperaturerange",
                verbose_name="Temperature",
            ),
        ),
        migrations.AddField(
            model_name="prescriptionfueltype",
            name="wind_direction",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="prescription_fuel_types",
                to="prescriptiondetails.winddirection",
                verbose_name="Wind Direction",
            ),
        ),
        migrations.AddField(
            model_name="prescriptionfueltype",
            name="wind_speed_range",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="prescription_fuel_types",
                to="prescriptiondetails.windspeedrange",
                verbose_name="Wind Speed",
            ),
        ),
    ]
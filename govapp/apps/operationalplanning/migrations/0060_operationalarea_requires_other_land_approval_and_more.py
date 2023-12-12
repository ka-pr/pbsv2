# Generated by Django 4.2.7 on 2023-12-01 07:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "operationalplanning",
            "0059_legalapproval_is_required_for_operational_area_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="operationalarea",
            name="requires_other_land_approval",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="operationalarea",
            name="requires_owner_approvals",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="operationalarea",
            name="requires_shire_approvals",
            field=models.BooleanField(default=False),
        ),
    ]

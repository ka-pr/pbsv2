# Generated by Django 4.2.6 on 2023-11-07 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0011_auto_load_lgas"),
        ("operationalplanning", "0007_remove_legalapproval_file_as_approval_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="legalapproval",
            name="lga",
        ),
        migrations.AddField(
            model_name="legalapproval",
            name="land_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("shire", "Shire"),
                    ("owner", "Owner"),
                    ("other", "Other Lands"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="operationalareaapproval",
            name="lga",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="operationalareaapprovals",
                to="main.lga",
            ),
        ),
    ]

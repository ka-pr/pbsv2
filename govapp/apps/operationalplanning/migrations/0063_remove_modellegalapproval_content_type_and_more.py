# Generated by Django 4.2.7 on 2023-12-04 08:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "operationalplanning",
            "0062_alter_operationalplanapproval_unique_together_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="modellegalapproval",
            name="content_type",
        ),
        migrations.RemoveField(
            model_name="modellegalapproval",
            name="legal_approval",
        ),
        migrations.RemoveField(
            model_name="modellegalapproval",
            name="lga",
        ),
        migrations.DeleteModel(
            name="LegalApproval",
        ),
        migrations.DeleteModel(
            name="ModelLegalApproval",
        ),
    ]

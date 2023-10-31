# Generated by Django 4.2.6 on 2023-10-31 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("operationalarea", "0002_operationalareariskfactor_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="operationalareaapproval",
            options={
                "verbose_name": "Operational Area Approval",
                "verbose_name_plural": "Operational Area Approvals",
            },
        ),
        migrations.RemoveField(
            model_name="operationalarea",
            name="risk_factors",
        ),
        migrations.AddField(
            model_name="operationalareariskfactor",
            name="operational_area",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="operationalarea.operationalarea",
            ),
        ),
    ]

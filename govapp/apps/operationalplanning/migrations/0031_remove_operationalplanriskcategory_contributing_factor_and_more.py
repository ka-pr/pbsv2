# Generated by Django 4.2.7 on 2023-11-15 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("risk", "0006_rename_riskfactor_riskcategory"),
        ("operationalplanning", "0030_operationalplanriskcategory_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="operationalplanriskcategory",
            name="contributing_factor",
        ),
        migrations.CreateModel(
            name="OperationalPlanRiskCategoryContributingFactor",
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
                    "contributing_factor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="risk.contributingfactor",
                    ),
                ),
                (
                    "operational_plan_risk_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="operationalplanning.operationalplanriskcategory",
                    ),
                ),
            ],
        ),
    ]

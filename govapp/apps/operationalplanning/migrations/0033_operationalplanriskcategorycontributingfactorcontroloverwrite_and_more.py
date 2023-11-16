# Generated by Django 4.2.7 on 2023-11-16 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("risk", "0009_alter_overwritecontrol_options_and_more"),
        (
            "operationalplanning",
            "0032_remove_operationalplanriskcategory_values_affected_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="OperationalPlanRiskCategoryContributingFactorControlOverwrite",
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
                    "operational_plan_risk_category_contributing_factor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="operational_plan_risk_category_contributing_factor_control_overwrites",
                        to="operationalplanning.operationalplanriskcategorycontributingfactor",
                    ),
                ),
                (
                    "overwrite_control",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="operational_plan_risk_category_contributing_factor_control_overwrites",
                        to="risk.overwritecontrol",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="operationalplanriskcategorycontributingfactor",
            name="contributing_factor_control_overwrites",
            field=models.ManyToManyField(
                editable=False,
                related_name="operational_plan_risk_category_contributing_factors",
                through="operationalplanning.OperationalPlanRiskCategoryContributingFactorControlOverwrite",
                to="risk.overwritecontrol",
            ),
        ),
    ]

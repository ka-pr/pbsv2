# Generated by Django 4.2.7 on 2023-12-08 06:22

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):
    dependencies = [
        ("operationalplanning", "0068_operationalplan_context_map"),
    ]

    operations = [
        migrations.AddField(
            model_name="operationalplan",
            name="status",
            field=model_utils.fields.StatusField(
                choices=[
                    ("draft", "Draft"),
                    ("with_district_officer", "With District Officer"),
                    (
                        "with_district_officer_referral",
                        "With District Officer (Referral)",
                    ),
                    ("with_regional_leader_fire", "With Regional Leader Fire"),
                    (
                        "with_regional_leader_fire_referral",
                        "With Regional Leader Fire (Referral)",
                    ),
                    ("with_fmsb_representative", "With FMSB Representative"),
                    ("with_district_manager", "With District Manager"),
                    ("with_regional_manager", "With Regional Manager"),
                    ("with_state_manager", "With State Manager"),
                    ("approved", "Approved"),
                ],
                default="draft",
                max_length=100,
                no_check_for_status=True,
                verbose_name="status",
            ),
        ),
        migrations.AddField(
            model_name="operationalplan",
            name="status_changed",
            field=model_utils.fields.MonitorField(
                default=django.utils.timezone.now,
                monitor="status",
                verbose_name="status changed",
            ),
        ),
    ]
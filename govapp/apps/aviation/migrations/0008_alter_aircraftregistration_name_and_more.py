# Generated by Django 4.2.6 on 2023-10-13 07:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("aviation", "0007_remove_aviationrequest_decision_files"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aircraftregistration",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="aircrafttype",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="ignitionmethod",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]

# Generated by Django 4.2.6 on 2023-10-31 02:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("risk", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="riskfactor",
            name="name",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
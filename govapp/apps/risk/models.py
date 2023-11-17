from logging import getLogger

from django.contrib.postgres.fields import DecimalRangeField
from django.db import models
from model_utils.models import TimeStampedModel

from govapp.apps.main.models import OrdinalScaleModel, UniqueNameableModel

logger = getLogger(__name__)


class Control(UniqueNameableModel, TimeStampedModel):
    class Meta:
        abstract = True


class StandardControl(Control):
    """Control that can be configured in the admin panel"""

    class Meta:
        verbose_name = "Control (Standard)"
        verbose_name_plural = "Controls (Standard)"


class OverwriteControl(Control):
    """Control to overwrite the default value of a standard control"""

    class Meta:
        verbose_name = "Control (Overwrite)"
        verbose_name_plural = "Controls (Overwrite)"

    standard_control = models.ForeignKey(
        "StandardControl",
        on_delete=models.PROTECT,
        related_name="overwrite_controls",
    )

    def __str__(self):
        return f"{self.name} (overwrites {self.standard_control.name})"


class AdditionalControl(Control):
    """Control that is only available when the resulting risk level of a risk assessment
    is configured as 'additional controls required'"""

    text = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Control (Additional)"
        verbose_name_plural = "Controls (Additional)"

    def __str__(self):
        return self.text


class ContributingFactorStandardControl(models.Model):
    class Meta:
        unique_together = ("contributing_factor", "standard_control")
        verbose_name = "Standard Control Default Value"
        verbose_name_plural = "Standard Control Default Values"

    contributing_factor = models.ForeignKey(
        "ContributingFactor",
        on_delete=models.PROTECT,
        related_name="contributing_factor_standard_controls",
    )
    standard_control = models.ForeignKey(
        "StandardControl",
        on_delete=models.PROTECT,
        related_name="contributing_factor_standard_controls",
    )
    revisit_in_implementation_plan = models.BooleanField(
        default=False
    )  # Whether control can be revisited in Implementation Plan


class ContributingFactor(UniqueNameableModel, TimeStampedModel):
    factors = DecimalRangeField(default_bounds="[)", blank=True, null=True)  # type: ignore
    standard_controls: models.ManyToManyField = models.ManyToManyField(
        StandardControl,
        related_name="contributing_factors",
        through="ContributingFactorStandardControl",
        through_fields=("contributing_factor", "standard_control"),
    )


class RiskCategory(UniqueNameableModel, TimeStampedModel):
    pass


class Consequence(UniqueNameableModel):
    pass


class Likelihood(OrdinalScaleModel):
    # lower_bound = IntervalFloatField(
    #     min_value=0.0, max_value=1.0, null=True, blank=True
    # )
    # upper_bound = IntervalFloatField(
    #     min_value=0.0, max_value=1.0, null=True, blank=True
    # )

    def __str__(self):
        return f"{self.name} ({self.ordinal_scale})"


class RiskLevel(OrdinalScaleModel):
    requires_additional_controls = models.BooleanField(default=False)


class LikelihoodOfConsequence(models.Model):
    consequence = models.ForeignKey(
        "Consequence",
        on_delete=models.PROTECT,
        related_name="likelihood_of_consequence",
    )
    likelihood = models.ForeignKey(
        "Likelihood",
        on_delete=models.PROTECT,
        related_name="likelihood_of_consequence",
    )
    risk_level = models.ForeignKey(
        "RiskLevel",
        on_delete=models.PROTECT,
        related_name="likelihood_of_consequence",
    )


class RiskRating(models.Model):
    consequence = models.ForeignKey(
        Consequence, on_delete=models.CASCADE, null=True, blank=True
    )
    likelihood = models.ForeignKey(
        Likelihood, on_delete=models.CASCADE, null=True, blank=True
    )

    @property
    def risk_level(self):
        return LikelihoodOfConsequence.objects.get(
            consequence=self.consequence, likelihood=self.likelihood
        ).risk_level

    def __str__(self):
        return f"{self.consequence.name} - Occurrence: {self.likelihood.name} (Risk level: {self.risk_level})"

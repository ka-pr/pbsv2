from django import forms
from django.contrib import admin
from model_utils import Choices

from govapp.apps.main.admin import DeleteRestrictedAdmin

from .models import (
    LegalApproval,
    OperationalArea,
    OperationalAreaRiskFactor,
    OperationalPlan,
    OperationalPlanApproval,
    OperationalPlanProgram,
    OperationalPlanPurpose,
)


class OperationalAreaPurposeInline(admin.TabularInline):
    model = OperationalPlanPurpose
    extra = 0


class OperationalAreaProgramInline(admin.TabularInline):
    model = OperationalPlanProgram
    extra = 0


class LegalApprovalAdminForm(forms.ModelForm):
    approval_type = forms.ChoiceField(
        choices=LegalApproval.APPROVAL_TYPES, required=True
    )  # This hides the null/empty option
    land_type = forms.ChoiceField(
        choices=Choices(("", "N/A")) + LegalApproval.LAND_TYPES, required=False
    )  # This adds a null/empty option

    class Meta:
        model = LegalApproval
        fields = "__all__"
        help_texts = {
            "has_additional_permissions": "Check to allow the user to attach a file as approval, "
            "provide free text as approval, or remove the required approval."
        }


@admin.register(LegalApproval)
class LegalApprovalAdmin(admin.ModelAdmin):
    model = LegalApproval
    form = LegalApprovalAdminForm

    list_display = (
        "approver",
        "approval_type",
        "land_type",
        "has_additional_permissions",
    )

    fieldsets = (
        (
            "General information",
            {
                "fields": (
                    (
                        "approver",
                        "approval_type",
                        "land_type",
                        "has_additional_permissions",
                    )
                ),
            },
        ),
    )


class OperationalAreaRiskFactorInline(admin.TabularInline):
    model = OperationalAreaRiskFactor
    extra = 0


class SelectWithOptionAttribute(forms.Select):
    def create_option(
        self, name, value, label, selected, index, subindex=None, attrs=None
    ):
        # This allows using strings labels as usual
        if isinstance(label, dict):
            opt_attrs = label.copy()
            label = opt_attrs.pop("label")
        else:
            opt_attrs = {}
        option_dict = super().create_option(
            name, value, label, selected, index, subindex=subindex, attrs=attrs
        )
        for key, val in opt_attrs.items():
            option_dict["attrs"][key] = val
        return option_dict


class OperationalAreaApprovalChoiceField(forms.ModelChoiceField):
    widget = SelectWithOptionAttribute

    def label_from_instance(self, obj):
        return {
            "label": super().label_from_instance(obj),
            "data-has-additional-permissions": str(obj.has_additional_permissions),
            "data-is-shire-approval": str(obj.is_shire_approval),
        }


class OperationalAreaApprovalAdminForm(forms.ModelForm):
    legal_approval = OperationalAreaApprovalChoiceField(
        queryset=LegalApproval.objects.all()
    )

    class Meta:
        model = OperationalPlanApproval
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()

        return cleaned_data


class OperationalAreaApprovalInline(admin.StackedInline):
    model = OperationalPlanApproval
    extra = 0
    verbose_name = "Operational Area Approval"
    verbose_name_plural = "Operational Area Approvals"

    form = OperationalAreaApprovalAdminForm

    class Media:
        js = (
            "admin/js/jquery.init.js",
            "admin/class_media/js/toggle_functions.js",
            "admin/class_media/js/operational_area_approval_admin.js",
        )
        css = {
            "all": ["admin/class_media/css/inline_fieldsets.css"],
        }

    class Meta:
        pass

    list_display = (
        "legal_approval",
        "file_as_approval",
        "has_additional_permissions",
        "text_as_approval",
        "text_remove_justification",
    )

    fieldsets = (
        (
            "Legal/Approval",
            {
                "fields": (("legal_approval",)),
                "classes": (
                    "legal-approval",
                    "less-dominant-style",
                ),
            },
        ),
        (
            "Land type",
            {
                "fields": (("lga",),),
                "classes": (
                    "additional-information-lga",
                    "less-dominant-style",
                    "hidden",
                ),
            },
        ),
        (
            "Documentation",
            {
                "fields": (
                    (
                        "file_as_approval",
                        "text_as_approval",
                        "text_remove_justification",
                    )
                ),
                "classes": (
                    "additional-information-docs",
                    "less-dominant-style",
                    "hidden",
                ),
            },
        ),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_formset(self, request, obj=None, **kwargs):
        form = super().get_formset(request, obj, **kwargs)

        return form


class OperationalAreaAdminForm(forms.ModelForm):
    class Meta:
        model = OperationalArea
        fields = "__all__"
        help_texts = {
            "operational_area_different_from_bpu_rationale": "Rationale when operational area is different "
            "from burn planning unit."
        }


@admin.register(OperationalArea)
class OperationalAreaAdmin(DeleteRestrictedAdmin):
    model = OperationalArea

    form = OperationalAreaAdminForm

    class Media:
        js = (
            "admin/js/jquery.init.js",
            "admin/class_media/js/toggle_functions.js",
            "admin/class_media/js/operational_area_admin.js",
        )

    list_display = (
        "name",
        "burn_plan_element",
        "year",
        "operational_area_different_from_bpu_rationale",
        "district",
        "contentious_burn",
        "contentious_rationale",
    )

    fieldsets = (
        (
            "Details",
            {
                "fields": (
                    "name",
                    "burn_plan_element",
                    "year",
                    "operational_area_different_from_bpu_rationale",
                    "contentious_burn",
                ),
            },
        ),
        (
            "Contentious burn",
            {
                "fields": (("contentious_rationale",),),
                "classes": (
                    "admin-contentious-burn",
                    "less-dominant-style",
                ),
            },
        ),
        (
            "Spatial",
            {
                "fields": (
                    "district",
                    (
                        "polygon",
                        "linestring",
                    ),
                ),
            },
        ),
    )

    inlines = [OperationalAreaRiskFactorInline]


@admin.register(OperationalPlan)
class OperationalPlanAdmin(DeleteRestrictedAdmin):
    model = OperationalPlan
    # form = OperationalAreaAdminForm

    list_display = (
        "name",
        "operational_area",
        "operation_name",
        "operation",
        "operational_intent",
        "burn_priority",
    )

    fieldsets = (
        (
            "Overview",
            {
                "fields": (
                    "name",
                    (
                        "reference_number",
                        "created",
                        "modified",
                    ),
                    "operational_area",
                    "operation_name",
                    "operation",
                    "operational_intent",
                    "burn_priority",
                ),
            },
        ),
    )

    readonly_fields = ("reference_number", "created", "modified")

    inlines = [
        OperationalAreaPurposeInline,
        OperationalAreaProgramInline,
        OperationalAreaApprovalInline,
    ]
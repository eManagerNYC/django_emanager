from django import forms
from . import models


class changeorderForm(forms.ModelForm):
    class Meta:
        model = models.changeorder
        fields = [
            "backup",
            "total_labor",
            "status",
            "exclusion_assumption",
            "total_material",
            "total_equipment",
            "change_amt",
            "work_scope",
            "tickets",
            "contract",
        ]


class ticketForm(forms.ModelForm):
    class Meta:
        model = models.ticket
        fields = [
            "total_cost",
            "work_start",
            "status",
            "work_shifts",
            "total_material",
            "work_end",
            "co_type",
            "total_labor",
            "co_reason",
            "labor_rate",
            "material_rate",
            "changeorder",
            "equipent_rate",
        ]


class contractsForm(forms.ModelForm):
    class Meta:
        model = models.contracts
        fields = [
            "contract_description",
            "attachment",
            "contract_file",
            "scheduleofvalues",
            "contract_type",
            "exclusion_assumption",
            "project",
            "company",
        ]


class requisitionForm(forms.ModelForm):
    class Meta:
        model = models.requisition
        fields = [
            "req_number",
            "req_amount",
            "coi",
            "stored_materials",
            "prev_amount",
            "lienwaiver",
            "company",
            "project",
        ]


class budgetForm(forms.ModelForm):
    class Meta:
        model = models.budget
        fields = [
            "line_code",
            "line_amount",
            "line_description",
            "project",
        ]

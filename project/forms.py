from django import forms
from . import models


class companyForm(forms.ModelForm):
    class Meta:
        model = models.company
        fields = [
            "company_address",
            "company_name",
            "company_phone",
            "division",
        ]


class projectsForm(forms.ModelForm):
    class Meta:
        model = models.projects
        fields = [
            "project_name",
        ]


class reportsForm(forms.ModelForm):
    class Meta:
        model = models.reports
        fields = []



class laborratesForm(forms.ModelForm):
    class Meta:
        model = models.laborrates
        fields = [
            "labor_cost",
            "labor_affiliation",
            "labor_name",
            "company",
        ]


class materialratesForm(forms.ModelForm):
    class Meta:
        model = models.materialrates
        fields = [
            "material_name",
            "material_cost",
            "company",
        ]


class equipmentratesForm(forms.ModelForm):
    class Meta:
        model = models.equipmentrates
        fields = [
            "equipment_cost",
            "equipment_name",
        ]


class divisionsForm(forms.ModelForm):
    class Meta:
        model = models.divisions
        fields = [
            "division_code",
            "division_name",
        ]

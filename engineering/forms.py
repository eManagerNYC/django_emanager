from django import forms
from . import models


class submittal_pkgForm(forms.ModelForm):
    class Meta:
        model = models.submittal_pkg
        fields = [
            "package_number",
            "submittals",
        ]


class rfiForm(forms.ModelForm):
    class Meta:
        model = models.rfi
        fields = [
            "status",
            "rfi_question",
            "duedate",
            "rfi_number",
            "rfi_answer",
            "rfi_co",
            "division",
        ]


class submittalForm(forms.ModelForm):
    class Meta:
        model = models.submittal
        fields = [
            "status",
            "submittal_file",
            "submittal_name",
            "duedate",
            "submittal_number",
            "division",
        ]

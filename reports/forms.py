from django import forms
from . import models


class reportsForm(forms.ModelForm):
    class Meta:
        model = models.reports
        fields = [
            "report_name",
        ]

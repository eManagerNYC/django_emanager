from django import forms
from . import models


class dailyreportForm(forms.ModelForm):
    class Meta:
        model = models.dailyreport
        fields = [
            "report_date",
        ]


class punchlistForm(forms.ModelForm):
    class Meta:
        model = models.punchlist
        fields = []



class checklistsForm(forms.ModelForm):
    class Meta:
        model = models.checklists
        fields = []


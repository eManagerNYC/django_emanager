from django import forms
from . import models


class scheduleForm(forms.ModelForm):
    class Meta:
        model = models.schedule
        fields = [
            "schedule_name",
            "tasks",
        ]


class taskForm(forms.ModelForm):
    class Meta:
        model = models.task
        fields = [
            "estimated_end",
            "actual_start",
            "task_name",
            "task_duration",
            "actual_end",
            "estimated_start",
            "predecessors",
            "successors",
        ]

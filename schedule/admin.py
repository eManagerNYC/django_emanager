from django.contrib import admin
from django import forms

from . import models


class scheduleAdminForm(forms.ModelForm):

    class Meta:
        model = models.schedule
        fields = "__all__"


class scheduleAdmin(admin.ModelAdmin):
    form = scheduleAdminForm
    list_display = [
        "created",
        "last_updated",
        "schedule_name",
    ]
    readonly_fields = [
        "created",
        "last_updated",
        "schedule_name",
    ]


class taskAdminForm(forms.ModelForm):

    class Meta:
        model = models.task
        fields = "__all__"


class taskAdmin(admin.ModelAdmin):
    form = taskAdminForm
    list_display = [
        "estimated_end",
        "actual_start",
        "last_updated",
        "created",
        "task_name",
        "task_duration",
        "actual_end",
        "estimated_start",
    ]
    readonly_fields = [
        "estimated_end",
        "actual_start",
        "last_updated",
        "created",
        "task_name",
        "task_duration",
        "actual_end",
        "estimated_start",
    ]


admin.site.register(models.schedule, scheduleAdmin)
admin.site.register(models.task, taskAdmin)

from django.contrib import admin
from django import forms

from . import models


class reportsAdminForm(forms.ModelForm):

    class Meta:
        model = models.reports
        fields = "__all__"


class reportsAdmin(admin.ModelAdmin):
    form = reportsAdminForm
    list_display = [
        "report_name",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "report_name",
        "last_updated",
        "created",
    ]


admin.site.register(models.reports, reportsAdmin)

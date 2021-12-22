from django.contrib import admin
from django import forms

from . import models


class dailyreportAdminForm(forms.ModelForm):

    class Meta:
        model = models.dailyreport
        fields = "__all__"


class dailyreportAdmin(admin.ModelAdmin):
    form = dailyreportAdminForm
    list_display = [
        "report_date",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "report_date",
        "created",
        "last_updated",
    ]


class punchlistAdminForm(forms.ModelForm):

    class Meta:
        model = models.punchlist
        fields = "__all__"


class punchlistAdmin(admin.ModelAdmin):
    form = punchlistAdminForm
    list_display = [
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "created",
    ]


class checklistsAdminForm(forms.ModelForm):

    class Meta:
        model = models.checklists
        fields = "__all__"


class checklistsAdmin(admin.ModelAdmin):
    form = checklistsAdminForm
    list_display = [
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


admin.site.register(models.dailyreport, dailyreportAdmin)
admin.site.register(models.punchlist, punchlistAdmin)
admin.site.register(models.checklists, checklistsAdmin)

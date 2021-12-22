from django.contrib import admin
from django import forms

from . import models


class submittal_pkgAdminForm(forms.ModelForm):

    class Meta:
        model = models.submittal_pkg
        fields = "__all__"


class submittal_pkgAdmin(admin.ModelAdmin):
    form = submittal_pkgAdminForm
    list_display = [
        "created",
        "last_updated",
        "package_number",
    ]
    readonly_fields = [
        "created",
        "last_updated",
        "package_number",
    ]


class rfiAdminForm(forms.ModelForm):

    class Meta:
        model = models.rfi
        fields = "__all__"


class rfiAdmin(admin.ModelAdmin):
    form = rfiAdminForm
    list_display = [
        "status",
        "rfi_question",
        "duedate",
        "rfi_number",
        "last_updated",
        "rfi_answer",
        "created",
    ]
    readonly_fields = [
        "status",
        "rfi_question",
        "duedate",
        "rfi_number",
        "last_updated",
        "rfi_answer",
        "created",
    ]


class submittalAdminForm(forms.ModelForm):

    class Meta:
        model = models.submittal
        fields = "__all__"


class submittalAdmin(admin.ModelAdmin):
    form = submittalAdminForm
    list_display = [
        "status",
        "submittal_file",
        "created",
        "submittal_name",
        "duedate",
        "submittal_number",
        "last_updated",
    ]
    readonly_fields = [
        "status",
        "submittal_file",
        "created",
        "submittal_name",
        "duedate",
        "submittal_number",
        "last_updated",
    ]


admin.site.register(models.submittal_pkg, submittal_pkgAdmin)
admin.site.register(models.rfi, rfiAdmin)
admin.site.register(models.submittal, submittalAdmin)

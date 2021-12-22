from django.contrib import admin
from django import forms

from . import models


class companyAdminForm(forms.ModelForm):

    class Meta:
        model = models.company
        fields = "__all__"


class companyAdmin(admin.ModelAdmin):
    form = companyAdminForm
    list_display = [
        "created",
        "company_address",
        "last_updated",
        "company_name",
        "company_phone",
    ]
    readonly_fields = [
        "created",
        "company_address",
        "last_updated",
        "company_name",
        "company_phone",
    ]


class projectsAdminForm(forms.ModelForm):

    class Meta:
        model = models.projects
        fields = "__all__"


class projectsAdmin(admin.ModelAdmin):
    form = projectsAdminForm
    list_display = [
        "created",
        "project_name",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "project_name",
        "last_updated",
    ]


class reportsAdminForm(forms.ModelForm):

    class Meta:
        model = models.reports
        fields = "__all__"


class reportsAdmin(admin.ModelAdmin):
    form = reportsAdminForm
    list_display = [
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class laborratesAdminForm(forms.ModelForm):

    class Meta:
        model = models.laborrates
        fields = "__all__"


class laborratesAdmin(admin.ModelAdmin):
    form = laborratesAdminForm
    list_display = [
        "last_updated",
        "labor_cost",
        "labor_affiliation",
        "labor_name",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "labor_cost",
        "labor_affiliation",
        "labor_name",
        "created",
    ]


class materialratesAdminForm(forms.ModelForm):

    class Meta:
        model = models.materialrates
        fields = "__all__"


class materialratesAdmin(admin.ModelAdmin):
    form = materialratesAdminForm
    list_display = [
        "created",
        "material_name",
        "last_updated",
        "material_cost",
    ]
    readonly_fields = [
        "created",
        "material_name",
        "last_updated",
        "material_cost",
    ]


class equipmentratesAdminForm(forms.ModelForm):

    class Meta:
        model = models.equipmentrates
        fields = "__all__"


class equipmentratesAdmin(admin.ModelAdmin):
    form = equipmentratesAdminForm
    list_display = [
        "last_updated",
        "created",
        "equipment_cost",
        "equipment_name",
    ]
    readonly_fields = [
        "last_updated",
        "created",
        "equipment_cost",
        "equipment_name",
    ]


class divisionsAdminForm(forms.ModelForm):

    class Meta:
        model = models.divisions
        fields = "__all__"


class divisionsAdmin(admin.ModelAdmin):
    form = divisionsAdminForm
    list_display = [
        "division_code",
        "created",
        "last_updated",
        "division_name",
    ]
    readonly_fields = [
        "division_code",
        "created",
        "last_updated",
        "division_name",
    ]


admin.site.register(models.company, companyAdmin)
admin.site.register(models.projects, projectsAdmin)
admin.site.register(models.reports, reportsAdmin)
admin.site.register(models.laborrates, laborratesAdmin)
admin.site.register(models.materialrates, materialratesAdmin)
admin.site.register(models.equipmentrates, equipmentratesAdmin)
admin.site.register(models.divisions, divisionsAdmin)

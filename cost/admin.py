from django.contrib import admin
from django import forms

from . import models


class changeorderAdminForm(forms.ModelForm):

    class Meta:
        model = models.changeorder
        fields = "__all__"


class changeorderAdmin(admin.ModelAdmin):
    form = changeorderAdminForm
    list_display = [
        "backup",
        "total_labor",
        "last_updated",
        "created",
        "status",
        "exclusion_assumption",
        "total_material",
        "total_equipment",
        "change_amt",
        "work_scope",
    ]
    readonly_fields = [
        "backup",
        "total_labor",
        "last_updated",
        "created",
        "status",
        "exclusion_assumption",
        "total_material",
        "total_equipment",
        "change_amt",
        "work_scope",
    ]


class ticketAdminForm(forms.ModelForm):

    class Meta:
        model = models.ticket
        fields = "__all__"


class ticketAdmin(admin.ModelAdmin):
    form = ticketAdminForm
    list_display = [
        "total_cost",
        "work_start",
        "status",
        "work_shifts",
        "created",
        "total_material",
        "work_end",
        "co_type",
        "last_updated",
        "total_labor",
        "co_reason",
    ]
    readonly_fields = [
        "total_cost",
        "work_start",
        "status",
        "work_shifts",
        "created",
        "total_material",
        "work_end",
        "co_type",
        "last_updated",
        "total_labor",
        "co_reason",
    ]


class contractsAdminForm(forms.ModelForm):

    class Meta:
        model = models.contracts
        fields = "__all__"


class contractsAdmin(admin.ModelAdmin):
    form = contractsAdminForm
    list_display = [
        "contract_description",
        "attachment",
        "contract_file",
        "created",
        "last_updated",
        "scheduleofvalues",
        "contract_type",
        "exclusion_assumption",
    ]
    readonly_fields = [
        "contract_description",
        "attachment",
        "contract_file",
        "created",
        "last_updated",
        "scheduleofvalues",
        "contract_type",
        "exclusion_assumption",
    ]


class requisitionAdminForm(forms.ModelForm):

    class Meta:
        model = models.requisition
        fields = "__all__"


class requisitionAdmin(admin.ModelAdmin):
    form = requisitionAdminForm
    list_display = [
        "created",
        "last_updated",
        "req_number",
        "req_amount",
        "coi",
        "stored_materials",
        "prev_amount",
        "lienwaiver",
    ]
    readonly_fields = [
        "created",
        "last_updated",
        "req_number",
        "req_amount",
        "coi",
        "stored_materials",
        "prev_amount",
        "lienwaiver",
    ]


class budgetAdminForm(forms.ModelForm):

    class Meta:
        model = models.budget
        fields = "__all__"


class budgetAdmin(admin.ModelAdmin):
    form = budgetAdminForm
    list_display = [
        "line_code",
        "line_amount",
        "last_updated",
        "created",
        "line_description",
    ]
    readonly_fields = [
        "line_code",
        "line_amount",
        "last_updated",
        "created",
        "line_description",
    ]


admin.site.register(models.changeorder, changeorderAdmin)
admin.site.register(models.ticket, ticketAdmin)
admin.site.register(models.contracts, contractsAdmin)
admin.site.register(models.requisition, requisitionAdmin)
admin.site.register(models.budget, budgetAdmin)

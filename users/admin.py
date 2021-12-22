from django.contrib import admin
from django import forms

from . import models


class usersAdminForm(forms.ModelForm):

    class Meta:
        model = models.users
        fields = "__all__"


class usersAdmin(admin.ModelAdmin):
    form = usersAdminForm
    list_display = [
        "last_updated",
        "useremail",
        "username",
        "created",
        "password",
    ]
    readonly_fields = [
        "last_updated",
        "useremail",
        "username",
        "created",
        "password",
    ]


class rolesAdminForm(forms.ModelForm):

    class Meta:
        model = models.roles
        fields = "__all__"


class rolesAdmin(admin.ModelAdmin):
    form = rolesAdminForm
    list_display = [
        "created",
        "rolename",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "rolename",
        "last_updated",
    ]


admin.site.register(models.users, usersAdmin)
admin.site.register(models.roles, rolesAdmin)

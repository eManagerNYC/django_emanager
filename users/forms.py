from django import forms
from . import models


class usersForm(forms.ModelForm):
    class Meta:
        model = models.users
        fields = [
            "useremail",
            "username",
            "password",
        ]


class rolesForm(forms.ModelForm):
    class Meta:
        model = models.roles
        fields = [
            "rolename",
        ]

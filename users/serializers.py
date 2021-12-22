from rest_framework import serializers

from . import models


class usersSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.users
        fields = [
            "last_updated",
            "useremail",
            "username",
            "created",
            "password",
        ]

class rolesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.roles
        fields = [
            "created",
            "rolename",
            "last_updated",
        ]

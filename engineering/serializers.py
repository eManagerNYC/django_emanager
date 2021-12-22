from rest_framework import serializers

from . import models


class submittal_pkgSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.submittal_pkg
        fields = [
            "created",
            "last_updated",
            "package_number",
        ]

class rfiSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.rfi
        fields = [
            "status",
            "rfi_question",
            "duedate",
            "rfi_number",
            "last_updated",
            "rfi_answer",
            "created",
        ]

class submittalSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.submittal
        fields = [
            "status",
            "submittal_file",
            "created",
            "submittal_name",
            "duedate",
            "submittal_number",
            "last_updated",
        ]

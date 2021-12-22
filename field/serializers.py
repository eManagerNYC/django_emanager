from rest_framework import serializers

from . import models


class dailyreportSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.dailyreport
        fields = [
            "report_date",
            "created",
            "last_updated",
        ]

class punchlistSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.punchlist
        fields = [
            "last_updated",
            "created",
        ]

class checklistsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.checklists
        fields = [
            "created",
            "last_updated",
        ]

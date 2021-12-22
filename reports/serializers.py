from rest_framework import serializers

from . import models


class reportsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.reports
        fields = [
            "report_name",
            "last_updated",
            "created",
        ]

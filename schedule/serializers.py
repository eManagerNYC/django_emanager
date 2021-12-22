from rest_framework import serializers

from . import models


class scheduleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.schedule
        fields = [
            "created",
            "last_updated",
            "schedule_name",
        ]

class taskSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.task
        fields = [
            "estimated_end",
            "actual_start",
            "last_updated",
            "created",
            "task_name",
            "task_duration",
            "actual_end",
            "estimated_start",
        ]

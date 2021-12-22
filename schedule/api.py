from rest_framework import viewsets, permissions

from . import serializers
from . import models


class scheduleViewSet(viewsets.ModelViewSet):
    """ViewSet for the schedule class"""

    queryset = models.schedule.objects.all()
    serializer_class = serializers.scheduleSerializer
    permission_classes = [permissions.IsAuthenticated]


class taskViewSet(viewsets.ModelViewSet):
    """ViewSet for the task class"""

    queryset = models.task.objects.all()
    serializer_class = serializers.taskSerializer
    permission_classes = [permissions.IsAuthenticated]

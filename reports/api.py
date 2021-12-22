from rest_framework import viewsets, permissions

from . import serializers
from . import models


class reportsViewSet(viewsets.ModelViewSet):
    """ViewSet for the reports class"""

    queryset = models.reports.objects.all()
    serializer_class = serializers.reportsSerializer
    permission_classes = [permissions.IsAuthenticated]

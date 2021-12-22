from rest_framework import viewsets, permissions

from . import serializers
from . import models


class dailyreportViewSet(viewsets.ModelViewSet):
    """ViewSet for the dailyreport class"""

    queryset = models.dailyreport.objects.all()
    serializer_class = serializers.dailyreportSerializer
    permission_classes = [permissions.IsAuthenticated]


class punchlistViewSet(viewsets.ModelViewSet):
    """ViewSet for the punchlist class"""

    queryset = models.punchlist.objects.all()
    serializer_class = serializers.punchlistSerializer
    permission_classes = [permissions.IsAuthenticated]


class checklistsViewSet(viewsets.ModelViewSet):
    """ViewSet for the checklists class"""

    queryset = models.checklists.objects.all()
    serializer_class = serializers.checklistsSerializer
    permission_classes = [permissions.IsAuthenticated]

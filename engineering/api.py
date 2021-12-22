from rest_framework import viewsets, permissions

from . import serializers
from . import models


class submittal_pkgViewSet(viewsets.ModelViewSet):
    """ViewSet for the submittal_pkg class"""

    queryset = models.submittal_pkg.objects.all()
    serializer_class = serializers.submittal_pkgSerializer
    permission_classes = [permissions.IsAuthenticated]


class rfiViewSet(viewsets.ModelViewSet):
    """ViewSet for the rfi class"""

    queryset = models.rfi.objects.all()
    serializer_class = serializers.rfiSerializer
    permission_classes = [permissions.IsAuthenticated]


class submittalViewSet(viewsets.ModelViewSet):
    """ViewSet for the submittal class"""

    queryset = models.submittal.objects.all()
    serializer_class = serializers.submittalSerializer
    permission_classes = [permissions.IsAuthenticated]

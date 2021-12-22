from rest_framework import viewsets, permissions

from . import serializers
from . import models


class companyViewSet(viewsets.ModelViewSet):
    """ViewSet for the company class"""

    queryset = models.company.objects.all()
    serializer_class = serializers.companySerializer
    permission_classes = [permissions.IsAuthenticated]


class projectsViewSet(viewsets.ModelViewSet):
    """ViewSet for the projects class"""

    queryset = models.projects.objects.all()
    serializer_class = serializers.projectsSerializer
    permission_classes = [permissions.IsAuthenticated]


class reportsViewSet(viewsets.ModelViewSet):
    """ViewSet for the reports class"""

    queryset = models.reports.objects.all()
    serializer_class = serializers.reportsSerializer
    permission_classes = [permissions.IsAuthenticated]


class laborratesViewSet(viewsets.ModelViewSet):
    """ViewSet for the laborrates class"""

    queryset = models.laborrates.objects.all()
    serializer_class = serializers.laborratesSerializer
    permission_classes = [permissions.IsAuthenticated]


class materialratesViewSet(viewsets.ModelViewSet):
    """ViewSet for the materialrates class"""

    queryset = models.materialrates.objects.all()
    serializer_class = serializers.materialratesSerializer
    permission_classes = [permissions.IsAuthenticated]


class equipmentratesViewSet(viewsets.ModelViewSet):
    """ViewSet for the equipmentrates class"""

    queryset = models.equipmentrates.objects.all()
    serializer_class = serializers.equipmentratesSerializer
    permission_classes = [permissions.IsAuthenticated]


class divisionsViewSet(viewsets.ModelViewSet):
    """ViewSet for the divisions class"""

    queryset = models.divisions.objects.all()
    serializer_class = serializers.divisionsSerializer
    permission_classes = [permissions.IsAuthenticated]

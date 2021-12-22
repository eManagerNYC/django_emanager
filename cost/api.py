from rest_framework import viewsets, permissions

from . import serializers
from . import models


class changeorderViewSet(viewsets.ModelViewSet):
    """ViewSet for the changeorder class"""

    queryset = models.changeorder.objects.all()
    serializer_class = serializers.changeorderSerializer
    permission_classes = [permissions.IsAuthenticated]


class ticketViewSet(viewsets.ModelViewSet):
    """ViewSet for the ticket class"""

    queryset = models.ticket.objects.all()
    serializer_class = serializers.ticketSerializer
    permission_classes = [permissions.IsAuthenticated]


class contractsViewSet(viewsets.ModelViewSet):
    """ViewSet for the contracts class"""

    queryset = models.contracts.objects.all()
    serializer_class = serializers.contractsSerializer
    permission_classes = [permissions.IsAuthenticated]


class requisitionViewSet(viewsets.ModelViewSet):
    """ViewSet for the requisition class"""

    queryset = models.requisition.objects.all()
    serializer_class = serializers.requisitionSerializer
    permission_classes = [permissions.IsAuthenticated]


class budgetViewSet(viewsets.ModelViewSet):
    """ViewSet for the budget class"""

    queryset = models.budget.objects.all()
    serializer_class = serializers.budgetSerializer
    permission_classes = [permissions.IsAuthenticated]

from rest_framework import viewsets, permissions

from . import serializers
from . import models


class usersViewSet(viewsets.ModelViewSet):
    """ViewSet for the users class"""

    queryset = models.users.objects.all()
    serializer_class = serializers.usersSerializer
    permission_classes = [permissions.IsAuthenticated]


class rolesViewSet(viewsets.ModelViewSet):
    """ViewSet for the roles class"""

    queryset = models.roles.objects.all()
    serializer_class = serializers.rolesSerializer
    permission_classes = [permissions.IsAuthenticated]

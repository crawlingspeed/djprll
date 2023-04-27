from rest_framework import viewsets, permissions

from . import serializers
from . import models


class garnishmentViewSet(viewsets.ModelViewSet):
    """ViewSet for the garnishment class"""

    queryset = models.garnishment.objects.all()
    serializer_class = serializers.garnishmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class emprateViewSet(viewsets.ModelViewSet):
    """ViewSet for the emprate class"""

    queryset = models.emprate.objects.all()
    serializer_class = serializers.emprateSerializer
    permission_classes = [permissions.IsAuthenticated]


class employeeViewSet(viewsets.ModelViewSet):
    """ViewSet for the employee class"""

    queryset = models.employee.objects.all()
    serializer_class = serializers.employeeSerializer
    permission_classes = [permissions.IsAuthenticated]

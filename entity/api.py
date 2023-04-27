from rest_framework import viewsets, permissions

from . import serializers
from . import models


class shiftViewSet(viewsets.ModelViewSet):
    """ViewSet for the shift class"""

    queryset = models.shift.objects.all()
    serializer_class = serializers.shiftSerializer
    permission_classes = [permissions.IsAuthenticated]


class localitytaxViewSet(viewsets.ModelViewSet):
    """ViewSet for the localitytax class"""

    queryset = models.localitytax.objects.all()
    serializer_class = serializers.localitytaxSerializer
    permission_classes = [permissions.IsAuthenticated]


class bankViewSet(viewsets.ModelViewSet):
    """ViewSet for the bank class"""

    queryset = models.bank.objects.all()
    serializer_class = serializers.bankSerializer
    permission_classes = [permissions.IsAuthenticated]


class statetaxViewSet(viewsets.ModelViewSet):
    """ViewSet for the statetax class"""

    queryset = models.statetax.objects.all()
    serializer_class = serializers.statetaxSerializer
    permission_classes = [permissions.IsAuthenticated]


class earningViewSet(viewsets.ModelViewSet):
    """ViewSet for the earning class"""

    queryset = models.earning.objects.all()
    serializer_class = serializers.earningSerializer
    permission_classes = [permissions.IsAuthenticated]


class departmentViewSet(viewsets.ModelViewSet):
    """ViewSet for the department class"""

    queryset = models.department.objects.all()
    serializer_class = serializers.departmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class deductionViewSet(viewsets.ModelViewSet):
    """ViewSet for the deduction class"""

    queryset = models.deduction.objects.all()
    serializer_class = serializers.deductionSerializer
    permission_classes = [permissions.IsAuthenticated]


class companyViewSet(viewsets.ModelViewSet):
    """ViewSet for the company class"""

    queryset = models.company.objects.all()
    serializer_class = serializers.companySerializer
    permission_classes = [permissions.IsAuthenticated]


class agencyViewSet(viewsets.ModelViewSet):
    """ViewSet for the agency class"""

    queryset = models.agency.objects.all()
    serializer_class = serializers.agencySerializer
    permission_classes = [permissions.IsAuthenticated]


class unitViewSet(viewsets.ModelViewSet):
    """ViewSet for the unit class"""

    queryset = models.unit.objects.all()
    serializer_class = serializers.unitSerializer
    permission_classes = [permissions.IsAuthenticated]


class branchViewSet(viewsets.ModelViewSet):
    """ViewSet for the branch class"""

    queryset = models.branch.objects.all()
    serializer_class = serializers.branchSerializer
    permission_classes = [permissions.IsAuthenticated]

from rest_framework import serializers

from . import models


class shiftSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.shift
        fields = [
            "code",
            "shift_name",
        ]

class localitytaxSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.localitytax
        fields = [
            "locality_rate",
            "locality",
        ]

class bankSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.bank
        fields = [
            "routing",
            "bank_name",
            "account",
            "aba",
        ]

class statetaxSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.statetax
        fields = [
            "sui_rate",
            "state",
            "sui_id",
            "state_id",
        ]

class earningSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.earning
        fields = [
            "created",
            "last_updated",
        ]

class departmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.department
        fields = [
        ]

class deductionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.deduction
        fields = [
            "pretax",
            "w2box14",
            "percent",
        ]

class companySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.company
        fields = [
            "taxpayer",
            "company_name",
            "created",
            "last_updated",
            "fed_id",
        ]

class agencySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.agency
        fields = [
            "name",
            "payee",
        ]

class unitSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.unit
        fields = [
        ]

class branchSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.branch
        fields = [
        ]

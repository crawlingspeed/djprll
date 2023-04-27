from rest_framework import serializers

from . import models


class garnishmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.garnishment
        fields = [
            "issuing_phone",
            "end_date",
            "amount_type",
            "limitamount",
            "isactive",
            "issuing_name",
            "orderid",
            "caseid",
            "release_date",
            "start_date",
            "issuing_title",
            "amount",
        ]

class emprateSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.emprate
        fields = [
            "rate",
            "isactive",
            "paytype",
        ]

class employeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.employee
        fields = [
            "paytype",
            "taxid",
            "birthdate",
            "created",
            "status",
            "payrate",
            "gender",
            "middle_name",
            "first_name",
            "timeclock_id",
            "card_id",
            "last_name",
            "taxid_type",
        ]

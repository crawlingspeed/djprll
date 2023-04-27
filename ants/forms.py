from django import forms
from . import models


class garnishmentForm(forms.ModelForm):
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
            "agency",
        ]


class emprateForm(forms.ModelForm):
    class Meta:
        model = models.emprate
        fields = [
            "rate",
            "isactive",
            "paytype",
            "shift_id",
            "employee",
        ]


class employeeForm(forms.ModelForm):
    class Meta:
        model = models.employee
        fields = [
            "paytype",
            "taxid",
            "birthdate",
            "status",
            "payrate",
            "gender",
            "middle_name",
            "first_name",
            "timeclock_id",
            "card_id",
            "last_name",
            "taxid_type",
            "branch",
            "localitytax",
            "department",
            "company",
            "statetax",
            "unit",
        ]

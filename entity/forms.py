from django import forms
from . import models


class shiftForm(forms.ModelForm):
    class Meta:
        model = models.shift
        fields = [
            "code",
            "shift_name",
            "branch",
            "company",
            "unit",
        ]


class localitytaxForm(forms.ModelForm):
    class Meta:
        model = models.localitytax
        fields = [
            "locality_rate",
            "locality",
            "company",
        ]


class bankForm(forms.ModelForm):
    class Meta:
        model = models.bank
        fields = [
            "routing",
            "bank_name",
            "account",
            "aba",
            "company",
            "branch",
        ]


class statetaxForm(forms.ModelForm):
    class Meta:
        model = models.statetax
        fields = [
            "sui_rate",
            "state",
            "sui_id",
            "state_id",
            "company",
        ]


class earningForm(forms.ModelForm):
    class Meta:
        model = models.earning
        fields = []



class departmentForm(forms.ModelForm):
    class Meta:
        model = models.department
        fields = [
            "company",
            "branch",
        ]


class deductionForm(forms.ModelForm):
    class Meta:
        model = models.deduction
        fields = [
            "pretax",
            "w2box14",
            "percent",
        ]


class companyForm(forms.ModelForm):
    class Meta:
        model = models.company
        fields = [
            "taxpayer",
            "company_name",
            "fed_id",
            "user",
        ]


class agencyForm(forms.ModelForm):
    class Meta:
        model = models.agency
        fields = [
            "name",
            "payee",
            "company",
        ]


class unitForm(forms.ModelForm):
    class Meta:
        model = models.unit
        fields = [
            "company",
            "department",
        ]


class branchForm(forms.ModelForm):
    class Meta:
        model = models.branch
        fields = [
            "company",
        ]

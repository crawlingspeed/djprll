from django.contrib import admin
from django import forms
from import_export.admin import ImportExportModelAdmin

from . import models


class garnishmentAdminForm(forms.ModelForm):

    class Meta:
        model = models.garnishment
        fields = "__all__"


class garnishmentAdmin(admin.ModelAdmin):
    form = garnishmentAdminForm
    list_display = [
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
    readonly_fields = [
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


class emprateAdminForm(forms.ModelForm):

    class Meta:
        model = models.emprate
        fields = "__all__"


class emprateAdmin(admin.ModelAdmin):
    form = emprateAdminForm
    list_display = [
        "rate",
        "isactive",
        "paytype",
    ]
    readonly_fields = [
        "rate",
        "isactive",
        "paytype",
    ]


class employeeAdminForm(forms.ModelForm):

    class Meta:
        model = models.employee
        fields = "__all__"


class employeeAdmin(ImportExportModelAdmin):
    form = employeeAdminForm
    list_display = [
        "first_name",
        "middle_name",
        "last_name",
        "card_id",
        "taxid",
        
        "paytype",
        "payrate",
        
        "status",

    ]
    readonly_fields = [
        "created",
    ]
    fields = [
        "company",
        "branch",
        "department",
        "unit",

        
        "card_id",
        
        "first_name",
        "middle_name",
        "last_name",
        "address",
        "address2",
        "city",
        "state",
        "postal",
        "phone",
        
        "birthdate",
        "gender",
        
        "taxid_type",
        "taxid",
        
        "paytype",
        "payrate",
        
        "status",
        
        "timeclock_id",
        
        "created",
    ]

admin.site.register(models.garnishment, garnishmentAdmin)
admin.site.register(models.emprate, emprateAdmin)
admin.site.register(models.employee, employeeAdmin)

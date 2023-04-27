from django.contrib import admin
from django import forms
from import_export.admin import ImportExportModelAdmin


from . import models



class shiftAdminForm(forms.ModelForm):

    class Meta:
        model = models.shift
        fields = "__all__"


class shiftAdmin(admin.ModelAdmin):
    form = shiftAdminForm
    list_display = [
        "code",
        "shift_name",
    ]
    readonly_fields = [

    ]


class localitytaxAdminForm(forms.ModelForm):

    class Meta:
        model = models.localitytax
        fields = "__all__"


class localitytaxAdmin(admin.ModelAdmin):
    form = localitytaxAdminForm
    list_display = [
        "locality_rate",
        "locality",
    ]
    readonly_fields = [

    ]


class bankAdminForm(forms.ModelForm):

    class Meta:
        model = models.bank
        fields = "__all__"


class bankAdmin(admin.ModelAdmin):
    form = bankAdminForm
    list_display = [
        "routing",
        "bank_name",
        "account",
        "aba",
    ]
    readonly_fields = [

    ]


class statetaxAdminForm(forms.ModelForm):

    class Meta:
        model = models.statetax
        fields = "__all__"


class statetaxAdmin(admin.ModelAdmin):
    form = statetaxAdminForm
    list_display = [
        "sui_rate",
        "state",
        "sui_id",
        "state_id",
    ]
    readonly_fields = [

    ]


class earningAdminForm(forms.ModelForm):

    class Meta:
        model = models.earning
        fields = "__all__"


class earningAdmin(admin.ModelAdmin):
    form = earningAdminForm
    list_display = [
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]


class departmentAdminForm(forms.ModelForm):

    class Meta:
        model = models.department
        fields = "__all__"


class departmentAdmin(admin.ModelAdmin):
    form = departmentAdminForm
    list_display = [
    ]
    readonly_fields = [
    ]


class deductionAdminForm(forms.ModelForm):

    class Meta:
        model = models.deduction
        fields = "__all__"


class deductionAdmin(admin.ModelAdmin):
    form = deductionAdminForm
    list_display = [
        "pretax",
        "w2box14",
        "percent",
    ]
    readonly_fields = [

    ]


class companyAdminForm(forms.ModelForm):

    class Meta:
        model = models.company
        fields = "__all__"


class companyAdmin(ImportExportModelAdmin):
    form = companyAdminForm
    list_display = [
        "taxpayer",
        "company_name",
        "created",
        "last_updated",
        "fed_id",
    ]
    readonly_fields = [
        "created",
        "last_updated",
    ]
    fields = [

        "company_name",
        "taxpayer",
        "fed_id",
        "address",
        "address2",
        "city",
        "state",
        "postal",
        "phone",
        
        "created",
        "last_updated",
        
    ]
    
    


class agencyAdminForm(forms.ModelForm):

    class Meta:
        model = models.agency
        fields = "__all__"


class agencyAdmin(admin.ModelAdmin):
    form = agencyAdminForm
    list_display = [
        "name",
        "payee",
    ]
    readonly_fields = [

    ]


class unitAdminForm(forms.ModelForm):

    class Meta:
        model = models.unit
        fields = "__all__"


class unitAdmin(admin.ModelAdmin):
    form = unitAdminForm
    list_display = [
    ]
    readonly_fields = [
    ]


class branchAdminForm(forms.ModelForm):

    class Meta:
        model = models.branch
        fields = "__all__"


class branchAdmin(admin.ModelAdmin):
    form = branchAdminForm
    list_display = [
    ]
    readonly_fields = [
    ]





admin.site.register(models.shift, shiftAdmin)
admin.site.register(models.localitytax, localitytaxAdmin)
admin.site.register(models.bank, bankAdmin)
admin.site.register(models.statetax, statetaxAdmin)
admin.site.register(models.earning, earningAdmin)
admin.site.register(models.department, departmentAdmin)
admin.site.register(models.deduction, deductionAdmin)
admin.site.register(models.company, companyAdmin)
admin.site.register(models.agency, agencyAdmin)
admin.site.register(models.unit, unitAdmin)
admin.site.register(models.branch, branchAdmin)


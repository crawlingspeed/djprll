from django.db import models
from django.urls import reverse

from common.models import contact

class garnishment(models.Model):

    # Relationships
    agency = models.ForeignKey("entity.agency", on_delete=models.CASCADE)

    # Fields
    issuing_phone = models.CharField(max_length=30)
    end_date = models.DateField()
    amount_type = models.CharField(max_length=1)
    limitamount = models.DecimalField(max_digits=10, decimal_places=2)
    isactive = models.BooleanField()
    issuing_name = models.CharField(max_length=30)
    orderid = models.CharField(max_length=30)
    caseid = models.CharField(max_length=30)
    release_date = models.DateField()
    start_date = models.DateField()
    issuing_title = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("ants_garnishment_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("ants_garnishment_update", args=(self.pk,))


class emprate(models.Model):

    # Relationships
    shift_id = models.ForeignKey("entity.shift", on_delete=models.CASCADE)
    employee = models.ForeignKey("ants.employee", on_delete=models.CASCADE)

    # Fields
    rate = models.DecimalField(max_digits=10, decimal_places=3)
    isactive = models.BooleanField()
    paytype = models.CharField(max_length=1)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("ants_emprate_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("ants_emprate_update", args=(self.pk,))


class employee(contact):

    # Relationships
    branch = models.ForeignKey("entity.branch", on_delete=models.CASCADE, null=True, blank=True)
    localitytax = models.OneToOneField("entity.localitytax", on_delete=models.SET_NULL, null=True, blank=True)
    department = models.ForeignKey("entity.department", on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey("entity.company", on_delete=models.CASCADE)
    statetax = models.OneToOneField("entity.statetax", on_delete=models.SET_NULL, null=True, blank=True)
    unit = models.ForeignKey("entity.unit", on_delete=models.CASCADE, null=True, blank=True)

    # Fields
    paytype = models.CharField(max_length=1, null=True, blank=True)
    taxid = models.CharField(max_length=30, null=True, blank=True)
    birthdate = models.CharField(max_length=10, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=True, blank=True)
    status = models.CharField(max_length=1, null=True, blank=True)
    payrate = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    first_name = models.CharField(max_length=30)
    timeclock_id = models.CharField(max_length=30, null=True, blank=True)
    card_id = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    last_name = models.CharField(max_length=30)
    taxid_type = models.CharField(max_length=3, null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.first_name)

    def get_absolute_url(self):
        return reverse("ants_employee_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("ants_employee_update", args=(self.pk,))

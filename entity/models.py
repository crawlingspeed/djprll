from django.db import models
from django.urls import reverse

from common.models import earningdeduction
from common.models import compartment
from common.models import contact

class shift(models.Model):

    # Relationships
    branch = models.ForeignKey("entity.branch", on_delete=models.CASCADE, null=True, blank=True)
    company = models.ForeignKey("entity.company", on_delete=models.CASCADE)
    unit = models.ForeignKey("entity.unit", on_delete=models.CASCADE, null=True, blank=True)

    # Fields
    code = models.CharField(max_length=30)
    shift_name = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("entity_shift_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("entity_shift_update", args=(self.pk,))


class localitytax(models.Model):

    # Relationships
    company = models.ForeignKey("entity.company", on_delete=models.CASCADE)

    # Fields
    locality_rate = models.DecimalField(max_digits=10, decimal_places=8)
    locality = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("entity_localitytax_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("entity_localitytax_update", args=(self.pk,))


class bank(models.Model):

    # Relationships
    company = models.ForeignKey("entity.company", on_delete=models.CASCADE)
    branch = models.ForeignKey("entity.branch", on_delete=models.CASCADE, null=True, blank=True)

    # Fields
    routing = models.CharField(max_length=30, null=True)
    bank_name = models.CharField(max_length=30, null=True)
    account = models.CharField(max_length=30, null=True)
    aba = models.CharField(max_length=10, null=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("entity_bank_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("entity_bank_update", args=(self.pk,))


class statetax(models.Model):

    # Relationships
    company = models.ForeignKey("entity.company", on_delete=models.CASCADE)

    # Fields
    sui_rate = models.DecimalField(max_digits=10, decimal_places=8, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    sui_id = models.CharField(max_length=30, null=True, blank=True)
    state_id = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("entity_statetax_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("entity_statetax_update", args=(self.pk,))


class earning(earningdeduction):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("entity_earning_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("entity_earning_update", args=(self.pk,))


class department(compartment):

    # Relationships
    company = models.ForeignKey("entity.company", on_delete=models.CASCADE)
    branch = models.ForeignKey("entity.branch", on_delete=models.CASCADE, null=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("entity_department_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("entity_department_update", args=(self.pk,))


class deduction(earningdeduction):

    # Fields
    pretax = models.BooleanField()
    w2box14 = models.BooleanField()
    percent = models.BooleanField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("entity_deduction_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("entity_deduction_update", args=(self.pk,))


class company(contact):

    # Relationships
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE, null=True)

    # Fields
    taxpayer = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    fed_id = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.company_name)

    def get_absolute_url(self):
        return reverse("entity_company_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("entity_company_update", args=(self.pk,))


class agency(contact):

    # Relationships
    company = models.ForeignKey("entity.company", on_delete=models.CASCADE)

    # Fields
    name = models.CharField(max_length=30)
    payee = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("entity_agency_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("entity_agency_update", args=(self.pk,))


class unit(compartment):

    # Relationships
    company = models.ForeignKey("entity.company", on_delete=models.CASCADE)
    department = models.ForeignKey("entity.department", on_delete=models.CASCADE, null=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("entity_unit_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("entity_unit_update", args=(self.pk,))


class branch(contact, compartment):

    # Relationships
    company = models.ForeignKey("entity.company", on_delete=models.CASCADE)
    note = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.cname)

    def get_absolute_url(self):
        return reverse("entity_branch_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("entity_branch_update", args=(self.pk,))

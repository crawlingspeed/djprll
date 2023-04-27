from django.db import models
from django.urls import reverse


class contact(models.Model):

    # Fields
    state = models.CharField(max_length=2, null=True, blank=True)
    postal = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    address2 = models.CharField(max_length=30, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("common_contact_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("common_contact_update", args=(self.pk,))


class compartment(models.Model):

    # Fields
    order = models.IntegerField()
    code = models.CharField(max_length=10)
    cname = models.CharField(max_length=30)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("common_compartment_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("common_compartment_update", args=(self.pk,))


class earningdeduction(models.Model):

    # Fields
    description = models.CharField(max_length=30)
    code = models.CharField(max_length=10)
    type = models.CharField(max_length=1)
    order = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("common_earningdeduction_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("common_earningdeduction_update", args=(self.pk,))

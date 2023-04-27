from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class garnishmentListView(generic.ListView):
    model = models.garnishment
    form_class = forms.garnishmentForm


class garnishmentCreateView(generic.CreateView):
    model = models.garnishment
    form_class = forms.garnishmentForm


class garnishmentDetailView(generic.DetailView):
    model = models.garnishment
    form_class = forms.garnishmentForm


class garnishmentUpdateView(generic.UpdateView):
    model = models.garnishment
    form_class = forms.garnishmentForm
    pk_url_kwarg = "pk"


class garnishmentDeleteView(generic.DeleteView):
    model = models.garnishment
    success_url = reverse_lazy("ants_garnishment_list")


class emprateListView(generic.ListView):
    model = models.emprate
    form_class = forms.emprateForm


class emprateCreateView(generic.CreateView):
    model = models.emprate
    form_class = forms.emprateForm


class emprateDetailView(generic.DetailView):
    model = models.emprate
    form_class = forms.emprateForm


class emprateUpdateView(generic.UpdateView):
    model = models.emprate
    form_class = forms.emprateForm
    pk_url_kwarg = "pk"


class emprateDeleteView(generic.DeleteView):
    model = models.emprate
    success_url = reverse_lazy("ants_emprate_list")


class employeeListView(generic.ListView):
    model = models.employee
    form_class = forms.employeeForm


class employeeCreateView(generic.CreateView):
    model = models.employee
    form_class = forms.employeeForm


class employeeDetailView(generic.DetailView):
    model = models.employee
    form_class = forms.employeeForm


class employeeUpdateView(generic.UpdateView):
    model = models.employee
    form_class = forms.employeeForm
    pk_url_kwarg = "pk"


class employeeDeleteView(generic.DeleteView):
    model = models.employee
    success_url = reverse_lazy("ants_employee_list")

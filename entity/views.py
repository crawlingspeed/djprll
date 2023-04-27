from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class shiftListView(generic.ListView):
    model = models.shift
    form_class = forms.shiftForm


class shiftCreateView(generic.CreateView):
    model = models.shift
    form_class = forms.shiftForm


class shiftDetailView(generic.DetailView):
    model = models.shift
    form_class = forms.shiftForm


class shiftUpdateView(generic.UpdateView):
    model = models.shift
    form_class = forms.shiftForm
    pk_url_kwarg = "pk"


class shiftDeleteView(generic.DeleteView):
    model = models.shift
    success_url = reverse_lazy("entity_shift_list")


class localitytaxListView(generic.ListView):
    model = models.localitytax
    form_class = forms.localitytaxForm


class localitytaxCreateView(generic.CreateView):
    model = models.localitytax
    form_class = forms.localitytaxForm


class localitytaxDetailView(generic.DetailView):
    model = models.localitytax
    form_class = forms.localitytaxForm


class localitytaxUpdateView(generic.UpdateView):
    model = models.localitytax
    form_class = forms.localitytaxForm
    pk_url_kwarg = "pk"


class localitytaxDeleteView(generic.DeleteView):
    model = models.localitytax
    success_url = reverse_lazy("entity_localitytax_list")


class bankListView(generic.ListView):
    model = models.bank
    form_class = forms.bankForm


class bankCreateView(generic.CreateView):
    model = models.bank
    form_class = forms.bankForm


class bankDetailView(generic.DetailView):
    model = models.bank
    form_class = forms.bankForm


class bankUpdateView(generic.UpdateView):
    model = models.bank
    form_class = forms.bankForm
    pk_url_kwarg = "pk"


class bankDeleteView(generic.DeleteView):
    model = models.bank
    success_url = reverse_lazy("entity_bank_list")


class statetaxListView(generic.ListView):
    model = models.statetax
    form_class = forms.statetaxForm


class statetaxCreateView(generic.CreateView):
    model = models.statetax
    form_class = forms.statetaxForm


class statetaxDetailView(generic.DetailView):
    model = models.statetax
    form_class = forms.statetaxForm


class statetaxUpdateView(generic.UpdateView):
    model = models.statetax
    form_class = forms.statetaxForm
    pk_url_kwarg = "pk"


class statetaxDeleteView(generic.DeleteView):
    model = models.statetax
    success_url = reverse_lazy("entity_statetax_list")


class earningListView(generic.ListView):
    model = models.earning
    form_class = forms.earningForm


class earningCreateView(generic.CreateView):
    model = models.earning
    form_class = forms.earningForm


class earningDetailView(generic.DetailView):
    model = models.earning
    form_class = forms.earningForm


class earningUpdateView(generic.UpdateView):
    model = models.earning
    form_class = forms.earningForm
    pk_url_kwarg = "pk"


class earningDeleteView(generic.DeleteView):
    model = models.earning
    success_url = reverse_lazy("entity_earning_list")


class departmentListView(generic.ListView):
    model = models.department
    form_class = forms.departmentForm


class departmentCreateView(generic.CreateView):
    model = models.department
    form_class = forms.departmentForm


class departmentDetailView(generic.DetailView):
    model = models.department
    form_class = forms.departmentForm


class departmentUpdateView(generic.UpdateView):
    model = models.department
    form_class = forms.departmentForm
    pk_url_kwarg = "pk"


class departmentDeleteView(generic.DeleteView):
    model = models.department
    success_url = reverse_lazy("entity_department_list")


class deductionListView(generic.ListView):
    model = models.deduction
    form_class = forms.deductionForm


class deductionCreateView(generic.CreateView):
    model = models.deduction
    form_class = forms.deductionForm


class deductionDetailView(generic.DetailView):
    model = models.deduction
    form_class = forms.deductionForm


class deductionUpdateView(generic.UpdateView):
    model = models.deduction
    form_class = forms.deductionForm
    pk_url_kwarg = "pk"


class deductionDeleteView(generic.DeleteView):
    model = models.deduction
    success_url = reverse_lazy("entity_deduction_list")


class companyListView(generic.ListView):
    model = models.company
    form_class = forms.companyForm


class companyCreateView(generic.CreateView):
    model = models.company
    form_class = forms.companyForm


class companyDetailView(generic.DetailView):
    model = models.company
    form_class = forms.companyForm


class companyUpdateView(generic.UpdateView):
    model = models.company
    form_class = forms.companyForm
    pk_url_kwarg = "pk"


class companyDeleteView(generic.DeleteView):
    model = models.company
    success_url = reverse_lazy("entity_company_list")


class agencyListView(generic.ListView):
    model = models.agency
    form_class = forms.agencyForm


class agencyCreateView(generic.CreateView):
    model = models.agency
    form_class = forms.agencyForm


class agencyDetailView(generic.DetailView):
    model = models.agency
    form_class = forms.agencyForm


class agencyUpdateView(generic.UpdateView):
    model = models.agency
    form_class = forms.agencyForm
    pk_url_kwarg = "pk"


class agencyDeleteView(generic.DeleteView):
    model = models.agency
    success_url = reverse_lazy("entity_agency_list")


class unitListView(generic.ListView):
    model = models.unit
    form_class = forms.unitForm


class unitCreateView(generic.CreateView):
    model = models.unit
    form_class = forms.unitForm


class unitDetailView(generic.DetailView):
    model = models.unit
    form_class = forms.unitForm


class unitUpdateView(generic.UpdateView):
    model = models.unit
    form_class = forms.unitForm
    pk_url_kwarg = "pk"


class unitDeleteView(generic.DeleteView):
    model = models.unit
    success_url = reverse_lazy("entity_unit_list")


class branchListView(generic.ListView):
    model = models.branch
    form_class = forms.branchForm

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(company_id=self.kwargs['company_id'])

class branchCreateView(generic.CreateView):
    model = models.branch
    form_class = forms.branchForm


class branchDetailView(generic.DetailView):
    model = models.branch
    form_class = forms.branchForm


class branchUpdateView(generic.UpdateView):
    model = models.branch
    form_class = forms.branchForm
    pk_url_kwarg = "pk"


class branchDeleteView(generic.DeleteView):
    model = models.branch
    success_url = reverse_lazy("entity_branch_list")


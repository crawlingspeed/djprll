from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("shift", api.shiftViewSet)
router.register("localitytax", api.localitytaxViewSet)
router.register("bank", api.bankViewSet)
router.register("statetax", api.statetaxViewSet)
router.register("earning", api.earningViewSet)
router.register("department", api.departmentViewSet)
router.register("deduction", api.deductionViewSet)
router.register("company", api.companyViewSet)
router.register("agency", api.agencyViewSet)
router.register("unit", api.unitViewSet)
router.register("branch", api.branchViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("entity/shift/", views.shiftListView.as_view(), name="entity_shift_list"),
    path("entity/shift/create/", views.shiftCreateView.as_view(), name="entity_shift_create"),
    path("entity/shift/detail/<int:pk>/", views.shiftDetailView.as_view(), name="entity_shift_detail"),
    path("entity/shift/update/<int:pk>/", views.shiftUpdateView.as_view(), name="entity_shift_update"),
    path("entity/shift/delete/<int:pk>/", views.shiftDeleteView.as_view(), name="entity_shift_delete"),
    path("entity/localitytax/", views.localitytaxListView.as_view(), name="entity_localitytax_list"),
    path("entity/localitytax/create/", views.localitytaxCreateView.as_view(), name="entity_localitytax_create"),
    path("entity/localitytax/detail/<int:pk>/", views.localitytaxDetailView.as_view(), name="entity_localitytax_detail"),
    path("entity/localitytax/update/<int:pk>/", views.localitytaxUpdateView.as_view(), name="entity_localitytax_update"),
    path("entity/localitytax/delete/<int:pk>/", views.localitytaxDeleteView.as_view(), name="entity_localitytax_delete"),
    path("entity/bank/", views.bankListView.as_view(), name="entity_bank_list"),
    path("entity/bank/create/", views.bankCreateView.as_view(), name="entity_bank_create"),
    path("entity/bank/detail/<int:pk>/", views.bankDetailView.as_view(), name="entity_bank_detail"),
    path("entity/bank/update/<int:pk>/", views.bankUpdateView.as_view(), name="entity_bank_update"),
    path("entity/bank/delete/<int:pk>/", views.bankDeleteView.as_view(), name="entity_bank_delete"),
    path("entity/statetax/", views.statetaxListView.as_view(), name="entity_statetax_list"),
    path("entity/statetax/create/", views.statetaxCreateView.as_view(), name="entity_statetax_create"),
    path("entity/statetax/detail/<int:pk>/", views.statetaxDetailView.as_view(), name="entity_statetax_detail"),
    path("entity/statetax/update/<int:pk>/", views.statetaxUpdateView.as_view(), name="entity_statetax_update"),
    path("entity/statetax/delete/<int:pk>/", views.statetaxDeleteView.as_view(), name="entity_statetax_delete"),
    path("entity/earning/", views.earningListView.as_view(), name="entity_earning_list"),
    path("entity/earning/create/", views.earningCreateView.as_view(), name="entity_earning_create"),
    path("entity/earning/detail/<int:pk>/", views.earningDetailView.as_view(), name="entity_earning_detail"),
    path("entity/earning/update/<int:pk>/", views.earningUpdateView.as_view(), name="entity_earning_update"),
    path("entity/earning/delete/<int:pk>/", views.earningDeleteView.as_view(), name="entity_earning_delete"),
    path("entity/department/", views.departmentListView.as_view(), name="entity_department_list"),
    path("entity/department/create/", views.departmentCreateView.as_view(), name="entity_department_create"),
    path("entity/department/detail/<int:pk>/", views.departmentDetailView.as_view(), name="entity_department_detail"),
    path("entity/department/update/<int:pk>/", views.departmentUpdateView.as_view(), name="entity_department_update"),
    path("entity/department/delete/<int:pk>/", views.departmentDeleteView.as_view(), name="entity_department_delete"),
    path("entity/deduction/", views.deductionListView.as_view(), name="entity_deduction_list"),
    path("entity/deduction/create/", views.deductionCreateView.as_view(), name="entity_deduction_create"),
    path("entity/deduction/detail/<int:pk>/", views.deductionDetailView.as_view(), name="entity_deduction_detail"),
    path("entity/deduction/update/<int:pk>/", views.deductionUpdateView.as_view(), name="entity_deduction_update"),
    path("entity/deduction/delete/<int:pk>/", views.deductionDeleteView.as_view(), name="entity_deduction_delete"),
    path("entity/company/", views.companyListView.as_view(), name="entity_company_list"),
    path("entity/company/create/", views.companyCreateView.as_view(), name="entity_company_create"),
    path("entity/company/detail/<int:pk>/", views.companyDetailView.as_view(), name="entity_company_detail"),
    path("entity/company/update/<int:pk>/", views.companyUpdateView.as_view(), name="entity_company_update"),
    path("entity/company/delete/<int:pk>/", views.companyDeleteView.as_view(), name="entity_company_delete"),
    path("entity/agency/", views.agencyListView.as_view(), name="entity_agency_list"),
    path("entity/agency/create/", views.agencyCreateView.as_view(), name="entity_agency_create"),
    path("entity/agency/detail/<int:pk>/", views.agencyDetailView.as_view(), name="entity_agency_detail"),
    path("entity/agency/update/<int:pk>/", views.agencyUpdateView.as_view(), name="entity_agency_update"),
    path("entity/agency/delete/<int:pk>/", views.agencyDeleteView.as_view(), name="entity_agency_delete"),
    path("entity/unit/", views.unitListView.as_view(), name="entity_unit_list"),
    path("entity/unit/create/", views.unitCreateView.as_view(), name="entity_unit_create"),
    path("entity/unit/detail/<int:pk>/", views.unitDetailView.as_view(), name="entity_unit_detail"),
    path("entity/unit/update/<int:pk>/", views.unitUpdateView.as_view(), name="entity_unit_update"),
    path("entity/unit/delete/<int:pk>/", views.unitDeleteView.as_view(), name="entity_unit_delete"),
    path("entity/branch/", views.branchListView.as_view(), name="entity_branch_list"),
    path("entity/branch/create/", views.branchCreateView.as_view(), name="entity_branch_create"),
    path("entity/branch/detail/<int:pk>/", views.branchDetailView.as_view(), name="entity_branch_detail"),
    path("entity/branch/update/<int:pk>/", views.branchUpdateView.as_view(), name="entity_branch_update"),
    path("entity/branch/delete/<int:pk>/", views.branchDeleteView.as_view(), name="entity_branch_delete"),

    path("companycheck/", views.companyListView.as_view(), name="entity_company_list"),
    path("companycheck/<int:pk>/", views.companyDetailView.as_view(), name="entity_company_detail"),
    path("companycheck/<int:company_id>/branch/", views.branchListView.as_view(), name="entity_branch_list"),
)

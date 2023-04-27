from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("garnishment", api.garnishmentViewSet)
router.register("emprate", api.emprateViewSet)
router.register("employee", api.employeeViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("ants/garnishment/", views.garnishmentListView.as_view(), name="ants_garnishment_list"),
    path("ants/garnishment/create/", views.garnishmentCreateView.as_view(), name="ants_garnishment_create"),
    path("ants/garnishment/detail/<int:pk>/", views.garnishmentDetailView.as_view(), name="ants_garnishment_detail"),
    path("ants/garnishment/update/<int:pk>/", views.garnishmentUpdateView.as_view(), name="ants_garnishment_update"),
    path("ants/garnishment/delete/<int:pk>/", views.garnishmentDeleteView.as_view(), name="ants_garnishment_delete"),
    path("ants/emprate/", views.emprateListView.as_view(), name="ants_emprate_list"),
    path("ants/emprate/create/", views.emprateCreateView.as_view(), name="ants_emprate_create"),
    path("ants/emprate/detail/<int:pk>/", views.emprateDetailView.as_view(), name="ants_emprate_detail"),
    path("ants/emprate/update/<int:pk>/", views.emprateUpdateView.as_view(), name="ants_emprate_update"),
    path("ants/emprate/delete/<int:pk>/", views.emprateDeleteView.as_view(), name="ants_emprate_delete"),
    path("ants/employee/", views.employeeListView.as_view(), name="ants_employee_list"),
    path("ants/employee/create/", views.employeeCreateView.as_view(), name="ants_employee_create"),
    path("ants/employee/detail/<int:pk>/", views.employeeDetailView.as_view(), name="ants_employee_detail"),
    path("ants/employee/update/<int:pk>/", views.employeeUpdateView.as_view(), name="ants_employee_update"),
    path("ants/employee/delete/<int:pk>/", views.employeeDeleteView.as_view(), name="ants_employee_delete"),
)

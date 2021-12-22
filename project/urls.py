from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("company", api.companyViewSet)
router.register("projects", api.projectsViewSet)
router.register("reports", api.reportsViewSet)
router.register("laborrates", api.laborratesViewSet)
router.register("materialrates", api.materialratesViewSet)
router.register("equipmentrates", api.equipmentratesViewSet)
router.register("divisions", api.divisionsViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("project/company/", views.companyListView.as_view(), name="project_company_list"),
    path("project/company/create/", views.companyCreateView.as_view(), name="project_company_create"),
    path("project/company/detail/<int:pk>/", views.companyDetailView.as_view(), name="project_company_detail"),
    path("project/company/update/<int:pk>/", views.companyUpdateView.as_view(), name="project_company_update"),
    path("project/company/delete/<int:pk>/", views.companyDeleteView.as_view(), name="project_company_delete"),
    path("project/projects/", views.projectsListView.as_view(), name="project_projects_list"),
    path("project/projects/create/", views.projectsCreateView.as_view(), name="project_projects_create"),
    path("project/projects/detail/<slug:project_name>/", views.projectsDetailView.as_view(), name="project_projects_detail"),
    path("project/projects/update/<slug:project_name>/", views.projectsUpdateView.as_view(), name="project_projects_update"),
    path("project/projects/delete/<slug:project_name>/", views.projectsDeleteView.as_view(), name="project_projects_delete"),
    path("project/reports/", views.reportsListView.as_view(), name="project_reports_list"),
    path("project/reports/create/", views.reportsCreateView.as_view(), name="project_reports_create"),
    path("project/reports/detail/<int:pk>/", views.reportsDetailView.as_view(), name="project_reports_detail"),
    path("project/reports/update/<int:pk>/", views.reportsUpdateView.as_view(), name="project_reports_update"),
    path("project/reports/delete/<int:pk>/", views.reportsDeleteView.as_view(), name="project_reports_delete"),
    path("project/laborrates/", views.laborratesListView.as_view(), name="project_laborrates_list"),
    path("project/laborrates/create/", views.laborratesCreateView.as_view(), name="project_laborrates_create"),
    path("project/laborrates/detail/<int:pk>/", views.laborratesDetailView.as_view(), name="project_laborrates_detail"),
    path("project/laborrates/update/<int:pk>/", views.laborratesUpdateView.as_view(), name="project_laborrates_update"),
    path("project/laborrates/delete/<int:pk>/", views.laborratesDeleteView.as_view(), name="project_laborrates_delete"),
    path("project/materialrates/", views.materialratesListView.as_view(), name="project_materialrates_list"),
    path("project/materialrates/create/", views.materialratesCreateView.as_view(), name="project_materialrates_create"),
    path("project/materialrates/detail/<int:pk>/", views.materialratesDetailView.as_view(), name="project_materialrates_detail"),
    path("project/materialrates/update/<int:pk>/", views.materialratesUpdateView.as_view(), name="project_materialrates_update"),
    path("project/materialrates/delete/<int:pk>/", views.materialratesDeleteView.as_view(), name="project_materialrates_delete"),
    path("project/equipmentrates/", views.equipmentratesListView.as_view(), name="project_equipmentrates_list"),
    path("project/equipmentrates/create/", views.equipmentratesCreateView.as_view(), name="project_equipmentrates_create"),
    path("project/equipmentrates/detail/<int:pk>/", views.equipmentratesDetailView.as_view(), name="project_equipmentrates_detail"),
    path("project/equipmentrates/update/<int:pk>/", views.equipmentratesUpdateView.as_view(), name="project_equipmentrates_update"),
    path("project/equipmentrates/delete/<int:pk>/", views.equipmentratesDeleteView.as_view(), name="project_equipmentrates_delete"),
    path("project/divisions/", views.divisionsListView.as_view(), name="project_divisions_list"),
    path("project/divisions/create/", views.divisionsCreateView.as_view(), name="project_divisions_create"),
    path("project/divisions/detail/<int:pk>/", views.divisionsDetailView.as_view(), name="project_divisions_detail"),
    path("project/divisions/update/<int:pk>/", views.divisionsUpdateView.as_view(), name="project_divisions_update"),
    path("project/divisions/delete/<int:pk>/", views.divisionsDeleteView.as_view(), name="project_divisions_delete"),
)

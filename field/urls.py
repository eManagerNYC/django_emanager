from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("dailyreport", api.dailyreportViewSet)
router.register("punchlist", api.punchlistViewSet)
router.register("checklists", api.checklistsViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("field/dailyreport/", views.dailyreportListView.as_view(), name="field_dailyreport_list"),
    path("field/dailyreport/create/", views.dailyreportCreateView.as_view(), name="field_dailyreport_create"),
    path("field/dailyreport/detail/<int:pk>/", views.dailyreportDetailView.as_view(), name="field_dailyreport_detail"),
    path("field/dailyreport/update/<int:pk>/", views.dailyreportUpdateView.as_view(), name="field_dailyreport_update"),
    path("field/dailyreport/delete/<int:pk>/", views.dailyreportDeleteView.as_view(), name="field_dailyreport_delete"),
    path("field/punchlist/", views.punchlistListView.as_view(), name="field_punchlist_list"),
    path("field/punchlist/create/", views.punchlistCreateView.as_view(), name="field_punchlist_create"),
    path("field/punchlist/detail/<int:pk>/", views.punchlistDetailView.as_view(), name="field_punchlist_detail"),
    path("field/punchlist/update/<int:pk>/", views.punchlistUpdateView.as_view(), name="field_punchlist_update"),
    path("field/punchlist/delete/<int:pk>/", views.punchlistDeleteView.as_view(), name="field_punchlist_delete"),
    path("field/checklists/", views.checklistsListView.as_view(), name="field_checklists_list"),
    path("field/checklists/create/", views.checklistsCreateView.as_view(), name="field_checklists_create"),
    path("field/checklists/detail/<int:pk>/", views.checklistsDetailView.as_view(), name="field_checklists_detail"),
    path("field/checklists/update/<int:pk>/", views.checklistsUpdateView.as_view(), name="field_checklists_update"),
    path("field/checklists/delete/<int:pk>/", views.checklistsDeleteView.as_view(), name="field_checklists_delete"),
)

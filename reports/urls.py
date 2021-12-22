from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("reports", api.reportsViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("reports/reports/", views.reportsListView.as_view(), name="reports_reports_list"),
    path("reports/reports/create/", views.reportsCreateView.as_view(), name="reports_reports_create"),
    path("reports/reports/detail/<int:pk>/", views.reportsDetailView.as_view(), name="reports_reports_detail"),
    path("reports/reports/update/<int:pk>/", views.reportsUpdateView.as_view(), name="reports_reports_update"),
    path("reports/reports/delete/<int:pk>/", views.reportsDeleteView.as_view(), name="reports_reports_delete"),
)

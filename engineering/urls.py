from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("submittal_pkg", api.submittal_pkgViewSet)
router.register("rfi", api.rfiViewSet)
router.register("submittal", api.submittalViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("engineering/submittal_pkg/", views.submittal_pkgListView.as_view(), name="engineering_submittal_pkg_list"),
    path("engineering/submittal_pkg/create/", views.submittal_pkgCreateView.as_view(), name="engineering_submittal_pkg_create"),
    path("engineering/submittal_pkg/detail/<int:pk>/", views.submittal_pkgDetailView.as_view(), name="engineering_submittal_pkg_detail"),
    path("engineering/submittal_pkg/update/<int:pk>/", views.submittal_pkgUpdateView.as_view(), name="engineering_submittal_pkg_update"),
    path("engineering/submittal_pkg/delete/<int:pk>/", views.submittal_pkgDeleteView.as_view(), name="engineering_submittal_pkg_delete"),
    path("engineering/rfi/", views.rfiListView.as_view(), name="engineering_rfi_list"),
    path("engineering/rfi/create/", views.rfiCreateView.as_view(), name="engineering_rfi_create"),
    path("engineering/rfi/detail/<int:pk>/", views.rfiDetailView.as_view(), name="engineering_rfi_detail"),
    path("engineering/rfi/update/<int:pk>/", views.rfiUpdateView.as_view(), name="engineering_rfi_update"),
    path("engineering/rfi/delete/<int:pk>/", views.rfiDeleteView.as_view(), name="engineering_rfi_delete"),
    path("engineering/submittal/", views.submittalListView.as_view(), name="engineering_submittal_list"),
    path("engineering/submittal/create/", views.submittalCreateView.as_view(), name="engineering_submittal_create"),
    path("engineering/submittal/detail/<int:pk>/", views.submittalDetailView.as_view(), name="engineering_submittal_detail"),
    path("engineering/submittal/update/<int:pk>/", views.submittalUpdateView.as_view(), name="engineering_submittal_update"),
    path("engineering/submittal/delete/<int:pk>/", views.submittalDeleteView.as_view(), name="engineering_submittal_delete"),
)

from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("users", api.usersViewSet)
router.register("roles", api.rolesViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("users/users/", views.usersListView.as_view(), name="users_users_list"),
    path("users/users/create/", views.usersCreateView.as_view(), name="users_users_create"),
    path("users/users/detail/<int:pk>/", views.usersDetailView.as_view(), name="users_users_detail"),
    path("users/users/update/<int:pk>/", views.usersUpdateView.as_view(), name="users_users_update"),
    path("users/users/delete/<int:pk>/", views.usersDeleteView.as_view(), name="users_users_delete"),
    path("users/roles/", views.rolesListView.as_view(), name="users_roles_list"),
    path("users/roles/create/", views.rolesCreateView.as_view(), name="users_roles_create"),
    path("users/roles/detail/<int:pk>/", views.rolesDetailView.as_view(), name="users_roles_detail"),
    path("users/roles/update/<int:pk>/", views.rolesUpdateView.as_view(), name="users_roles_update"),
    path("users/roles/delete/<int:pk>/", views.rolesDeleteView.as_view(), name="users_roles_delete"),
)

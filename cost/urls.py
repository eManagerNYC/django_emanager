from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("changeorder", api.changeorderViewSet)
router.register("ticket", api.ticketViewSet)
router.register("contracts", api.contractsViewSet)
router.register("requisition", api.requisitionViewSet)
router.register("budget", api.budgetViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("cost/changeorder/", views.changeorderListView.as_view(), name="cost_changeorder_list"),
    path("cost/changeorder/create/", views.changeorderCreateView.as_view(), name="cost_changeorder_create"),
    path("cost/changeorder/detail/<int:pk>/", views.changeorderDetailView.as_view(), name="cost_changeorder_detail"),
    path("cost/changeorder/update/<int:pk>/", views.changeorderUpdateView.as_view(), name="cost_changeorder_update"),
    path("cost/changeorder/delete/<int:pk>/", views.changeorderDeleteView.as_view(), name="cost_changeorder_delete"),
    path("cost/ticket/", views.ticketListView.as_view(), name="cost_ticket_list"),
    path("cost/ticket/create/", views.ticketCreateView.as_view(), name="cost_ticket_create"),
    path("cost/ticket/detail/<int:pk>/", views.ticketDetailView.as_view(), name="cost_ticket_detail"),
    path("cost/ticket/update/<int:pk>/", views.ticketUpdateView.as_view(), name="cost_ticket_update"),
    path("cost/ticket/delete/<int:pk>/", views.ticketDeleteView.as_view(), name="cost_ticket_delete"),
    path("cost/contracts/", views.contractsListView.as_view(), name="cost_contracts_list"),
    path("cost/contracts/create/", views.contractsCreateView.as_view(), name="cost_contracts_create"),
    path("cost/contracts/detail/<int:pk>/", views.contractsDetailView.as_view(), name="cost_contracts_detail"),
    path("cost/contracts/update/<int:pk>/", views.contractsUpdateView.as_view(), name="cost_contracts_update"),
    path("cost/contracts/delete/<int:pk>/", views.contractsDeleteView.as_view(), name="cost_contracts_delete"),
    path("cost/requisition/", views.requisitionListView.as_view(), name="cost_requisition_list"),
    path("cost/requisition/create/", views.requisitionCreateView.as_view(), name="cost_requisition_create"),
    path("cost/requisition/detail/<int:pk>/", views.requisitionDetailView.as_view(), name="cost_requisition_detail"),
    path("cost/requisition/update/<int:pk>/", views.requisitionUpdateView.as_view(), name="cost_requisition_update"),
    path("cost/requisition/delete/<int:pk>/", views.requisitionDeleteView.as_view(), name="cost_requisition_delete"),
    path("cost/budget/", views.budgetListView.as_view(), name="cost_budget_list"),
    path("cost/budget/create/", views.budgetCreateView.as_view(), name="cost_budget_create"),
    path("cost/budget/detail/<int:pk>/", views.budgetDetailView.as_view(), name="cost_budget_detail"),
    path("cost/budget/update/<int:pk>/", views.budgetUpdateView.as_view(), name="cost_budget_update"),
    path("cost/budget/delete/<int:pk>/", views.budgetDeleteView.as_view(), name="cost_budget_delete"),
)

from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class changeorderListView(generic.ListView):
    model = models.changeorder
    form_class = forms.changeorderForm


class changeorderCreateView(generic.CreateView):
    model = models.changeorder
    form_class = forms.changeorderForm


class changeorderDetailView(generic.DetailView):
    model = models.changeorder
    form_class = forms.changeorderForm


class changeorderUpdateView(generic.UpdateView):
    model = models.changeorder
    form_class = forms.changeorderForm
    pk_url_kwarg = "pk"


class changeorderDeleteView(generic.DeleteView):
    model = models.changeorder
    success_url = reverse_lazy("cost_changeorder_list")


class ticketListView(generic.ListView):
    model = models.ticket
    form_class = forms.ticketForm


class ticketCreateView(generic.CreateView):
    model = models.ticket
    form_class = forms.ticketForm


class ticketDetailView(generic.DetailView):
    model = models.ticket
    form_class = forms.ticketForm


class ticketUpdateView(generic.UpdateView):
    model = models.ticket
    form_class = forms.ticketForm
    pk_url_kwarg = "pk"


class ticketDeleteView(generic.DeleteView):
    model = models.ticket
    success_url = reverse_lazy("cost_ticket_list")


class contractsListView(generic.ListView):
    model = models.contracts
    form_class = forms.contractsForm


class contractsCreateView(generic.CreateView):
    model = models.contracts
    form_class = forms.contractsForm


class contractsDetailView(generic.DetailView):
    model = models.contracts
    form_class = forms.contractsForm


class contractsUpdateView(generic.UpdateView):
    model = models.contracts
    form_class = forms.contractsForm
    pk_url_kwarg = "pk"


class contractsDeleteView(generic.DeleteView):
    model = models.contracts
    success_url = reverse_lazy("cost_contracts_list")


class requisitionListView(generic.ListView):
    model = models.requisition
    form_class = forms.requisitionForm


class requisitionCreateView(generic.CreateView):
    model = models.requisition
    form_class = forms.requisitionForm


class requisitionDetailView(generic.DetailView):
    model = models.requisition
    form_class = forms.requisitionForm


class requisitionUpdateView(generic.UpdateView):
    model = models.requisition
    form_class = forms.requisitionForm
    pk_url_kwarg = "pk"


class requisitionDeleteView(generic.DeleteView):
    model = models.requisition
    success_url = reverse_lazy("cost_requisition_list")


class budgetListView(generic.ListView):
    model = models.budget
    form_class = forms.budgetForm


class budgetCreateView(generic.CreateView):
    model = models.budget
    form_class = forms.budgetForm


class budgetDetailView(generic.DetailView):
    model = models.budget
    form_class = forms.budgetForm


class budgetUpdateView(generic.UpdateView):
    model = models.budget
    form_class = forms.budgetForm
    pk_url_kwarg = "pk"


class budgetDeleteView(generic.DeleteView):
    model = models.budget
    success_url = reverse_lazy("cost_budget_list")

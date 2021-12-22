from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class dailyreportListView(generic.ListView):
    model = models.dailyreport
    form_class = forms.dailyreportForm


class dailyreportCreateView(generic.CreateView):
    model = models.dailyreport
    form_class = forms.dailyreportForm


class dailyreportDetailView(generic.DetailView):
    model = models.dailyreport
    form_class = forms.dailyreportForm


class dailyreportUpdateView(generic.UpdateView):
    model = models.dailyreport
    form_class = forms.dailyreportForm
    pk_url_kwarg = "pk"


class dailyreportDeleteView(generic.DeleteView):
    model = models.dailyreport
    success_url = reverse_lazy("field_dailyreport_list")


class punchlistListView(generic.ListView):
    model = models.punchlist
    form_class = forms.punchlistForm


class punchlistCreateView(generic.CreateView):
    model = models.punchlist
    form_class = forms.punchlistForm


class punchlistDetailView(generic.DetailView):
    model = models.punchlist
    form_class = forms.punchlistForm


class punchlistUpdateView(generic.UpdateView):
    model = models.punchlist
    form_class = forms.punchlistForm
    pk_url_kwarg = "pk"


class punchlistDeleteView(generic.DeleteView):
    model = models.punchlist
    success_url = reverse_lazy("field_punchlist_list")


class checklistsListView(generic.ListView):
    model = models.checklists
    form_class = forms.checklistsForm


class checklistsCreateView(generic.CreateView):
    model = models.checklists
    form_class = forms.checklistsForm


class checklistsDetailView(generic.DetailView):
    model = models.checklists
    form_class = forms.checklistsForm


class checklistsUpdateView(generic.UpdateView):
    model = models.checklists
    form_class = forms.checklistsForm
    pk_url_kwarg = "pk"


class checklistsDeleteView(generic.DeleteView):
    model = models.checklists
    success_url = reverse_lazy("field_checklists_list")

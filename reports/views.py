from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class reportsListView(generic.ListView):
    model = models.reports
    form_class = forms.reportsForm


class reportsCreateView(generic.CreateView):
    model = models.reports
    form_class = forms.reportsForm


class reportsDetailView(generic.DetailView):
    model = models.reports
    form_class = forms.reportsForm


class reportsUpdateView(generic.UpdateView):
    model = models.reports
    form_class = forms.reportsForm
    pk_url_kwarg = "pk"


class reportsDeleteView(generic.DeleteView):
    model = models.reports
    success_url = reverse_lazy("reports_reports_list")

from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class submittal_pkgListView(generic.ListView):
    model = models.submittal_pkg
    form_class = forms.submittal_pkgForm


class submittal_pkgCreateView(generic.CreateView):
    model = models.submittal_pkg
    form_class = forms.submittal_pkgForm


class submittal_pkgDetailView(generic.DetailView):
    model = models.submittal_pkg
    form_class = forms.submittal_pkgForm


class submittal_pkgUpdateView(generic.UpdateView):
    model = models.submittal_pkg
    form_class = forms.submittal_pkgForm
    pk_url_kwarg = "pk"


class submittal_pkgDeleteView(generic.DeleteView):
    model = models.submittal_pkg
    success_url = reverse_lazy("engineering_submittal_pkg_list")


class rfiListView(generic.ListView):
    model = models.rfi
    form_class = forms.rfiForm


class rfiCreateView(generic.CreateView):
    model = models.rfi
    form_class = forms.rfiForm


class rfiDetailView(generic.DetailView):
    model = models.rfi
    form_class = forms.rfiForm


class rfiUpdateView(generic.UpdateView):
    model = models.rfi
    form_class = forms.rfiForm
    pk_url_kwarg = "pk"


class rfiDeleteView(generic.DeleteView):
    model = models.rfi
    success_url = reverse_lazy("engineering_rfi_list")


class submittalListView(generic.ListView):
    model = models.submittal
    form_class = forms.submittalForm


class submittalCreateView(generic.CreateView):
    model = models.submittal
    form_class = forms.submittalForm


class submittalDetailView(generic.DetailView):
    model = models.submittal
    form_class = forms.submittalForm


class submittalUpdateView(generic.UpdateView):
    model = models.submittal
    form_class = forms.submittalForm
    pk_url_kwarg = "pk"


class submittalDeleteView(generic.DeleteView):
    model = models.submittal
    success_url = reverse_lazy("engineering_submittal_list")

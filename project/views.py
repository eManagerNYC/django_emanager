from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class companyListView(generic.ListView):
    model = models.company
    form_class = forms.companyForm


class companyCreateView(generic.CreateView):
    model = models.company
    form_class = forms.companyForm


class companyDetailView(generic.DetailView):
    model = models.company
    form_class = forms.companyForm


class companyUpdateView(generic.UpdateView):
    model = models.company
    form_class = forms.companyForm
    pk_url_kwarg = "pk"


class companyDeleteView(generic.DeleteView):
    model = models.company
    success_url = reverse_lazy("project_company_list")


class projectsListView(generic.ListView):
    model = models.projects
    form_class = forms.projectsForm


class projectsCreateView(generic.CreateView):
    model = models.projects
    form_class = forms.projectsForm


class projectsDetailView(generic.DetailView):
    model = models.projects
    form_class = forms.projectsForm
    pk_url_kwarg = "project_name"


class projectsUpdateView(generic.UpdateView):
    model = models.projects
    form_class = forms.projectsForm
    pk_url_kwarg = "project_name"


class projectsDeleteView(generic.DeleteView):
    model = models.projects
    success_url = reverse_lazy("project_projects_list")


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
    success_url = reverse_lazy("project_reports_list")


class laborratesListView(generic.ListView):
    model = models.laborrates
    form_class = forms.laborratesForm


class laborratesCreateView(generic.CreateView):
    model = models.laborrates
    form_class = forms.laborratesForm


class laborratesDetailView(generic.DetailView):
    model = models.laborrates
    form_class = forms.laborratesForm


class laborratesUpdateView(generic.UpdateView):
    model = models.laborrates
    form_class = forms.laborratesForm
    pk_url_kwarg = "pk"


class laborratesDeleteView(generic.DeleteView):
    model = models.laborrates
    success_url = reverse_lazy("project_laborrates_list")


class materialratesListView(generic.ListView):
    model = models.materialrates
    form_class = forms.materialratesForm


class materialratesCreateView(generic.CreateView):
    model = models.materialrates
    form_class = forms.materialratesForm


class materialratesDetailView(generic.DetailView):
    model = models.materialrates
    form_class = forms.materialratesForm


class materialratesUpdateView(generic.UpdateView):
    model = models.materialrates
    form_class = forms.materialratesForm
    pk_url_kwarg = "pk"


class materialratesDeleteView(generic.DeleteView):
    model = models.materialrates
    success_url = reverse_lazy("project_materialrates_list")


class equipmentratesListView(generic.ListView):
    model = models.equipmentrates
    form_class = forms.equipmentratesForm


class equipmentratesCreateView(generic.CreateView):
    model = models.equipmentrates
    form_class = forms.equipmentratesForm


class equipmentratesDetailView(generic.DetailView):
    model = models.equipmentrates
    form_class = forms.equipmentratesForm


class equipmentratesUpdateView(generic.UpdateView):
    model = models.equipmentrates
    form_class = forms.equipmentratesForm
    pk_url_kwarg = "pk"


class equipmentratesDeleteView(generic.DeleteView):
    model = models.equipmentrates
    success_url = reverse_lazy("project_equipmentrates_list")


class divisionsListView(generic.ListView):
    model = models.divisions
    form_class = forms.divisionsForm


class divisionsCreateView(generic.CreateView):
    model = models.divisions
    form_class = forms.divisionsForm


class divisionsDetailView(generic.DetailView):
    model = models.divisions
    form_class = forms.divisionsForm


class divisionsUpdateView(generic.UpdateView):
    model = models.divisions
    form_class = forms.divisionsForm
    pk_url_kwarg = "pk"


class divisionsDeleteView(generic.DeleteView):
    model = models.divisions
    success_url = reverse_lazy("project_divisions_list")

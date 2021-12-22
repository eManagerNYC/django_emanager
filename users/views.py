from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class usersListView(generic.ListView):
    model = models.users
    form_class = forms.usersForm


class usersCreateView(generic.CreateView):
    model = models.users
    form_class = forms.usersForm


class usersDetailView(generic.DetailView):
    model = models.users
    form_class = forms.usersForm


class usersUpdateView(generic.UpdateView):
    model = models.users
    form_class = forms.usersForm
    pk_url_kwarg = "pk"


class usersDeleteView(generic.DeleteView):
    model = models.users
    success_url = reverse_lazy("users_users_list")


class rolesListView(generic.ListView):
    model = models.roles
    form_class = forms.rolesForm


class rolesCreateView(generic.CreateView):
    model = models.roles
    form_class = forms.rolesForm


class rolesDetailView(generic.DetailView):
    model = models.roles
    form_class = forms.rolesForm


class rolesUpdateView(generic.UpdateView):
    model = models.roles
    form_class = forms.rolesForm
    pk_url_kwarg = "pk"


class rolesDeleteView(generic.DeleteView):
    model = models.roles
    success_url = reverse_lazy("users_roles_list")

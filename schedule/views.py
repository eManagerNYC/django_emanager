from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class scheduleListView(generic.ListView):
    model = models.schedule
    form_class = forms.scheduleForm


class scheduleCreateView(generic.CreateView):
    model = models.schedule
    form_class = forms.scheduleForm


class scheduleDetailView(generic.DetailView):
    model = models.schedule
    form_class = forms.scheduleForm


class scheduleUpdateView(generic.UpdateView):
    model = models.schedule
    form_class = forms.scheduleForm
    pk_url_kwarg = "pk"


class scheduleDeleteView(generic.DeleteView):
    model = models.schedule
    success_url = reverse_lazy("schedule_schedule_list")


class taskListView(generic.ListView):
    model = models.task
    form_class = forms.taskForm


class taskCreateView(generic.CreateView):
    model = models.task
    form_class = forms.taskForm


class taskDetailView(generic.DetailView):
    model = models.task
    form_class = forms.taskForm


class taskUpdateView(generic.UpdateView):
    model = models.task
    form_class = forms.taskForm
    pk_url_kwarg = "pk"


class taskDeleteView(generic.DeleteView):
    model = models.task
    success_url = reverse_lazy("schedule_task_list")

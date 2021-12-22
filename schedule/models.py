from django.db import models
from django.urls import reverse


class schedule(models.Model):

    # Relationships
    tasks = models.ManyToManyField("schedule.task")

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    schedule_name = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("schedule_schedule_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("schedule_schedule_update", args=(self.pk,))


class task(models.Model):

    # Relationships
    predecessors = models.ManyToManyField("schedule.task")
    successors = models.ManyToManyField("schedule.task")

    # Fields
    estimated_end = models.DateField()
    actual_start = models.DateField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    task_name = models.TextField(max_length=100)
    task_duration = models.IntegerField()
    actual_end = models.DateField()
    estimated_start = models.DateField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("schedule_task_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("schedule_task_update", args=(self.pk,))

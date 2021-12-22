from django.db import models
from django.urls import reverse


class reports(models.Model):

    # Fields
    report_name = models.TextField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("reports_reports_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("reports_reports_update", args=(self.pk,))

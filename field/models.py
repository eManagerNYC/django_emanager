from django.db import models
from django.urls import reverse


class dailyreport(models.Model):

    # Fields
    report_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("field_dailyreport_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("field_dailyreport_update", args=(self.pk,))


class punchlist(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("field_punchlist_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("field_punchlist_update", args=(self.pk,))


class checklists(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("field_checklists_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("field_checklists_update", args=(self.pk,))

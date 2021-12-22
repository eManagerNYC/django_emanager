from django.db import models
from django.urls import reverse


class submittal_pkg(models.Model):

    # Relationships
    submittals = models.ManyToManyField("engineering.submittal")

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    package_number = models.UUIDField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("engineering_submittal_pkg_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("engineering_submittal_pkg_update", args=(self.pk,))


class rfi(models.Model):

    # Relationships
    rfi_co = models.ForeignKey("cost.changeorder", on_delete=models.CASCADE)
    division = models.ForeignKey("project.divisions", on_delete=models.CASCADE)

    # Fields
    status = models.TextField(max_length=100)
    rfi_question = models.TextField(max_length=255)
    duedate = models.DateField()
    rfi_number = models.UUIDField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    rfi_answer = models.TextField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("engineering_rfi_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("engineering_rfi_update", args=(self.pk,))


class submittal(models.Model):

    # Relationships
    division = models.ForeignKey("project.divisions", on_delete=models.CASCADE)

    # Fields
    status = models.TextField(max_length=100)
    submittal_file = models.FileField(upload_to="upload/files/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    submittal_name = models.TextField(max_length=100)
    duedate = models.DateField()
    submittal_number = models.UUIDField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("engineering_submittal_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("engineering_submittal_update", args=(self.pk,))

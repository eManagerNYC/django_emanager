from django.db import models
from django.urls import reverse


class company(models.Model):

    # Relationships
    division = models.ForeignKey("project.Divisions", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    company_address = models.TextField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    company_name = models.TextField(max_length=100)
    company_phone = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("project_company_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("project_company_update", args=(self.pk,))


class projects(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    project_name = models.SlugField()
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("project_projects_detail", args=(self.project_name,))

    def get_update_url(self):
        return reverse("project_projects_update", args=(self.project_name,))


class reports(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("project_reports_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("project_reports_update", args=(self.pk,))


class laborrates(models.Model):

    # Relationships
    company = models.ForeignKey("project.company", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    labor_cost = models.TextField(max_length=100)
    labor_affiliation = models.TextField(max_length=100)
    labor_name = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("project_laborrates_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("project_laborrates_update", args=(self.pk,))


class materialrates(models.Model):

    # Relationships
    company = models.ForeignKey("project.company", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    material_name = models.TextField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    material_cost = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("project_materialrates_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("project_materialrates_update", args=(self.pk,))


class equipmentrates(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    equipment_cost = models.FloatField()
    equipment_name = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("project_equipmentrates_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("project_equipmentrates_update", args=(self.pk,))


class divisions(models.Model):

    # Fields
    division_code = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    division_name = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("project_divisions_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("project_divisions_update", args=(self.pk,))

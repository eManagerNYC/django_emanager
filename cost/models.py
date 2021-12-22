from django.db import models
from django.urls import reverse


class changeorder(models.Model):

    # Relationships
    tickets = models.ForeignKey("cost.ticket", on_delete=models.CASCADE)
    contract = models.ForeignKey("cost.contracts", on_delete=models.CASCADE)

    # Fields
    backup = models.URLField()
    total_labor = models.TextField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    status = models.TextField(max_length=100)
    exclusion_assumption = models.TextField(max_length=100)
    total_material = models.TextField(max_length=100)
    total_equipment = models.TextField(max_length=100)
    change_amt = models.FloatField()
    work_scope = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("cost_changeorder_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("cost_changeorder_update", args=(self.pk,))


class ticket(models.Model):

    # Relationships
    labor_rate = models.ManyToManyField("project.laborrates")
    material_rate = models.ManyToManyField("project.materialrates")
    changeorder = models.ForeignKey("cost.changeorder", on_delete=models.CASCADE)
    equipent_rate = models.OneToOneField("project.equipmentrates")

    # Fields
    total_cost = models.FloatField()
    work_start = models.DateTimeField()
    status = models.TextField(max_length=100)
    work_shifts = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    total_material = models.FloatField()
    work_end = models.DateTimeField()
    co_type = models.TextField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    total_labor = models.FloatField()
    co_reason = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("cost_ticket_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("cost_ticket_update", args=(self.pk,))


class contracts(models.Model):

    # Relationships
    project = models.ForeignKey("project.projects", on_delete=models.CASCADE)
    company = models.ForeignKey("project.company", on_delete=models.CASCADE)

    # Fields
    contract_description = models.TextField(max_length=255)
    attachment = models.URLField()
    contract_file = models.FileField(upload_to="upload/files/")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    scheduleofvalues = models.TextField(max_length=255)
    contract_type = models.TextField(max_length=100)
    exclusion_assumption = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("cost_contracts_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("cost_contracts_update", args=(self.pk,))


class requisition(models.Model):

    # Relationships
    company = models.ForeignKey("project.company", on_delete=models.CASCADE)
    project = models.ForeignKey("project.projects", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    req_number = models.TextField(max_length=100)
    req_amount = models.TextField(max_length=100)
    coi = models.URLField()
    stored_materials = models.FloatField()
    prev_amount = models.FloatField()
    lienwaiver = models.URLField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("cost_requisition_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("cost_requisition_update", args=(self.pk,))


class budget(models.Model):

    # Relationships
    project = models.ForeignKey("project.projects", on_delete=models.CASCADE)

    # Fields
    line_code = models.TextField(max_length=100)
    line_amount = models.TextField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    line_description = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("cost_budget_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("cost_budget_update", args=(self.pk,))

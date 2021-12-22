from django.db import models
from django.urls import reverse


class users(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    useremail = models.EmailField()
    username = models.UUIDField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    password = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("users_users_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("users_users_update", args=(self.pk,))


class roles(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    rolename = models.TextField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("users_roles_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("users_roles_update", args=(self.pk,))

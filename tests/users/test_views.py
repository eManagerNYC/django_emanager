import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_users_list_view():
    instance1 = test_helpers.create_users_users()
    instance2 = test_helpers.create_users_users()
    client = Client()
    url = reverse("users_users_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_users_create_view():
    client = Client()
    url = reverse("users_users_create")
    data = {
        "useremail": "user@tempurl.com",
        "username": "b297a243-b621-4907-8581-e9b3ac146a07",
        "password": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_users_detail_view():
    client = Client()
    instance = test_helpers.create_users_users()
    url = reverse("users_users_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_users_update_view():
    client = Client()
    instance = test_helpers.create_users_users()
    url = reverse("users_users_update", args=[instance.pk, ])
    data = {
        "useremail": "user@tempurl.com",
        "username": "b297a243-b621-4907-8581-e9b3ac146a07",
        "password": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_roles_list_view():
    instance1 = test_helpers.create_users_roles()
    instance2 = test_helpers.create_users_roles()
    client = Client()
    url = reverse("users_roles_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_roles_create_view():
    client = Client()
    url = reverse("users_roles_create")
    data = {
        "rolename": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_roles_detail_view():
    client = Client()
    instance = test_helpers.create_users_roles()
    url = reverse("users_roles_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_roles_update_view():
    client = Client()
    instance = test_helpers.create_users_roles()
    url = reverse("users_roles_update", args=[instance.pk, ])
    data = {
        "rolename": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302

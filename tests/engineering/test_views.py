import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_submittal_pkg_list_view():
    instance1 = test_helpers.create_engineering_submittal_pkg()
    instance2 = test_helpers.create_engineering_submittal_pkg()
    client = Client()
    url = reverse("engineering_submittal_pkg_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_submittal_pkg_create_view():
    submittals = test_helpers.create_engineering_submittal()
    client = Client()
    url = reverse("engineering_submittal_pkg_create")
    data = {
        "package_number": "b297a243-b621-4907-8581-e9b3ac146a07",
        "submittals": submittals.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_submittal_pkg_detail_view():
    client = Client()
    instance = test_helpers.create_engineering_submittal_pkg()
    url = reverse("engineering_submittal_pkg_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_submittal_pkg_update_view():
    submittals = test_helpers.create_engineering_submittal()
    client = Client()
    instance = test_helpers.create_engineering_submittal_pkg()
    url = reverse("engineering_submittal_pkg_update", args=[instance.pk, ])
    data = {
        "package_number": "b297a243-b621-4907-8581-e9b3ac146a07",
        "submittals": submittals.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_rfi_list_view():
    instance1 = test_helpers.create_engineering_rfi()
    instance2 = test_helpers.create_engineering_rfi()
    client = Client()
    url = reverse("engineering_rfi_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_rfi_create_view():
    rfi_co = test_helpers.create_cost_changeorder()
    division = test_helpers.create_project_divisions()
    client = Client()
    url = reverse("engineering_rfi_create")
    data = {
        "status": "text",
        "rfi_question": "text",
        "duedate": datetime.now(),
        "rfi_number": "b297a243-b621-4907-8581-e9b3ac146a07",
        "rfi_answer": "text",
        "rfi_co": rfi_co.pk,
        "division": division.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_rfi_detail_view():
    client = Client()
    instance = test_helpers.create_engineering_rfi()
    url = reverse("engineering_rfi_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_rfi_update_view():
    rfi_co = test_helpers.create_cost_changeorder()
    division = test_helpers.create_project_divisions()
    client = Client()
    instance = test_helpers.create_engineering_rfi()
    url = reverse("engineering_rfi_update", args=[instance.pk, ])
    data = {
        "status": "text",
        "rfi_question": "text",
        "duedate": datetime.now(),
        "rfi_number": "b297a243-b621-4907-8581-e9b3ac146a07",
        "rfi_answer": "text",
        "rfi_co": rfi_co.pk,
        "division": division.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_submittal_list_view():
    instance1 = test_helpers.create_engineering_submittal()
    instance2 = test_helpers.create_engineering_submittal()
    client = Client()
    url = reverse("engineering_submittal_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_submittal_create_view():
    division = test_helpers.create_project_divisions()
    client = Client()
    url = reverse("engineering_submittal_create")
    data = {
        "status": "text",
        "submittal_file": "aFile",
        "submittal_name": "text",
        "duedate": datetime.now(),
        "submittal_number": "b297a243-b621-4907-8581-e9b3ac146a07",
        "division": division.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_submittal_detail_view():
    client = Client()
    instance = test_helpers.create_engineering_submittal()
    url = reverse("engineering_submittal_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_submittal_update_view():
    division = test_helpers.create_project_divisions()
    client = Client()
    instance = test_helpers.create_engineering_submittal()
    url = reverse("engineering_submittal_update", args=[instance.pk, ])
    data = {
        "status": "text",
        "submittal_file": "aFile",
        "submittal_name": "text",
        "duedate": datetime.now(),
        "submittal_number": "b297a243-b621-4907-8581-e9b3ac146a07",
        "division": division.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302

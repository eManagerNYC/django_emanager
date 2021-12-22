import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_dailyreport_list_view():
    instance1 = test_helpers.create_field_dailyreport()
    instance2 = test_helpers.create_field_dailyreport()
    client = Client()
    url = reverse("field_dailyreport_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_dailyreport_create_view():
    client = Client()
    url = reverse("field_dailyreport_create")
    data = {
        "report_date": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_dailyreport_detail_view():
    client = Client()
    instance = test_helpers.create_field_dailyreport()
    url = reverse("field_dailyreport_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_dailyreport_update_view():
    client = Client()
    instance = test_helpers.create_field_dailyreport()
    url = reverse("field_dailyreport_update", args=[instance.pk, ])
    data = {
        "report_date": datetime.now(),
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_punchlist_list_view():
    instance1 = test_helpers.create_field_punchlist()
    instance2 = test_helpers.create_field_punchlist()
    client = Client()
    url = reverse("field_punchlist_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_punchlist_create_view():
    client = Client()
    url = reverse("field_punchlist_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_punchlist_detail_view():
    client = Client()
    instance = test_helpers.create_field_punchlist()
    url = reverse("field_punchlist_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_punchlist_update_view():
    client = Client()
    instance = test_helpers.create_field_punchlist()
    url = reverse("field_punchlist_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_checklists_list_view():
    instance1 = test_helpers.create_field_checklists()
    instance2 = test_helpers.create_field_checklists()
    client = Client()
    url = reverse("field_checklists_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_checklists_create_view():
    client = Client()
    url = reverse("field_checklists_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_checklists_detail_view():
    client = Client()
    instance = test_helpers.create_field_checklists()
    url = reverse("field_checklists_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_checklists_update_view():
    client = Client()
    instance = test_helpers.create_field_checklists()
    url = reverse("field_checklists_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302

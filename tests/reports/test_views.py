import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_reports_list_view():
    instance1 = test_helpers.create_reports_reports()
    instance2 = test_helpers.create_reports_reports()
    client = Client()
    url = reverse("reports_reports_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_reports_create_view():
    client = Client()
    url = reverse("reports_reports_create")
    data = {
        "report_name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_reports_detail_view():
    client = Client()
    instance = test_helpers.create_reports_reports()
    url = reverse("reports_reports_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_reports_update_view():
    client = Client()
    instance = test_helpers.create_reports_reports()
    url = reverse("reports_reports_update", args=[instance.pk, ])
    data = {
        "report_name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302

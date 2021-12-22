import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_company_list_view():
    instance1 = test_helpers.create_project_company()
    instance2 = test_helpers.create_project_company()
    client = Client()
    url = reverse("project_company_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_company_create_view():
    division = test_helpers.create_project_Divisions()
    client = Client()
    url = reverse("project_company_create")
    data = {
        "company_address": "text",
        "company_name": "text",
        "company_phone": "text",
        "division": division.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_company_detail_view():
    client = Client()
    instance = test_helpers.create_project_company()
    url = reverse("project_company_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_company_update_view():
    division = test_helpers.create_project_Divisions()
    client = Client()
    instance = test_helpers.create_project_company()
    url = reverse("project_company_update", args=[instance.pk, ])
    data = {
        "company_address": "text",
        "company_name": "text",
        "company_phone": "text",
        "division": division.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_projects_list_view():
    instance1 = test_helpers.create_project_projects()
    instance2 = test_helpers.create_project_projects()
    client = Client()
    url = reverse("project_projects_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_projects_create_view():
    client = Client()
    url = reverse("project_projects_create")
    data = {
        "project_name": "slug",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_projects_detail_view():
    client = Client()
    instance = test_helpers.create_project_projects()
    url = reverse("project_projects_detail", args=[instance.project_name, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_projects_update_view():
    client = Client()
    instance = test_helpers.create_project_projects()
    url = reverse("project_projects_update", args=[instance.project_name, ])
    data = {
        "project_name": "slug",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_reports_list_view():
    instance1 = test_helpers.create_project_reports()
    instance2 = test_helpers.create_project_reports()
    client = Client()
    url = reverse("project_reports_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_reports_create_view():
    client = Client()
    url = reverse("project_reports_create")
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_reports_detail_view():
    client = Client()
    instance = test_helpers.create_project_reports()
    url = reverse("project_reports_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_reports_update_view():
    client = Client()
    instance = test_helpers.create_project_reports()
    url = reverse("project_reports_update", args=[instance.pk, ])
    data = {
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_laborrates_list_view():
    instance1 = test_helpers.create_project_laborrates()
    instance2 = test_helpers.create_project_laborrates()
    client = Client()
    url = reverse("project_laborrates_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_laborrates_create_view():
    company = test_helpers.create_project_company()
    client = Client()
    url = reverse("project_laborrates_create")
    data = {
        "labor_cost": "text",
        "labor_affiliation": "text",
        "labor_name": "text",
        "company": company.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_laborrates_detail_view():
    client = Client()
    instance = test_helpers.create_project_laborrates()
    url = reverse("project_laborrates_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_laborrates_update_view():
    company = test_helpers.create_project_company()
    client = Client()
    instance = test_helpers.create_project_laborrates()
    url = reverse("project_laborrates_update", args=[instance.pk, ])
    data = {
        "labor_cost": "text",
        "labor_affiliation": "text",
        "labor_name": "text",
        "company": company.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_materialrates_list_view():
    instance1 = test_helpers.create_project_materialrates()
    instance2 = test_helpers.create_project_materialrates()
    client = Client()
    url = reverse("project_materialrates_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_materialrates_create_view():
    company = test_helpers.create_project_company()
    client = Client()
    url = reverse("project_materialrates_create")
    data = {
        "material_name": "text",
        "material_cost": "text",
        "company": company.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_materialrates_detail_view():
    client = Client()
    instance = test_helpers.create_project_materialrates()
    url = reverse("project_materialrates_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_materialrates_update_view():
    company = test_helpers.create_project_company()
    client = Client()
    instance = test_helpers.create_project_materialrates()
    url = reverse("project_materialrates_update", args=[instance.pk, ])
    data = {
        "material_name": "text",
        "material_cost": "text",
        "company": company.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_equipmentrates_list_view():
    instance1 = test_helpers.create_project_equipmentrates()
    instance2 = test_helpers.create_project_equipmentrates()
    client = Client()
    url = reverse("project_equipmentrates_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_equipmentrates_create_view():
    client = Client()
    url = reverse("project_equipmentrates_create")
    data = {
        "equipment_cost": 1.0f,
        "equipment_name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_equipmentrates_detail_view():
    client = Client()
    instance = test_helpers.create_project_equipmentrates()
    url = reverse("project_equipmentrates_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_equipmentrates_update_view():
    client = Client()
    instance = test_helpers.create_project_equipmentrates()
    url = reverse("project_equipmentrates_update", args=[instance.pk, ])
    data = {
        "equipment_cost": 1.0f,
        "equipment_name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_divisions_list_view():
    instance1 = test_helpers.create_project_divisions()
    instance2 = test_helpers.create_project_divisions()
    client = Client()
    url = reverse("project_divisions_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_divisions_create_view():
    client = Client()
    url = reverse("project_divisions_create")
    data = {
        "division_code": "text",
        "division_name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_divisions_detail_view():
    client = Client()
    instance = test_helpers.create_project_divisions()
    url = reverse("project_divisions_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_divisions_update_view():
    client = Client()
    instance = test_helpers.create_project_divisions()
    url = reverse("project_divisions_update", args=[instance.pk, ])
    data = {
        "division_code": "text",
        "division_name": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302

import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_changeorder_list_view():
    instance1 = test_helpers.create_cost_changeorder()
    instance2 = test_helpers.create_cost_changeorder()
    client = Client()
    url = reverse("cost_changeorder_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_changeorder_create_view():
    tickets = test_helpers.create_cost_ticket()
    contract = test_helpers.create_cost_contracts()
    client = Client()
    url = reverse("cost_changeorder_create")
    data = {
        "backup": http://127.0.0.1,
        "total_labor": "text",
        "status": "text",
        "exclusion_assumption": "text",
        "total_material": "text",
        "total_equipment": "text",
        "change_amt": 1.0f,
        "work_scope": "text",
        "tickets": tickets.pk,
        "contract": contract.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_changeorder_detail_view():
    client = Client()
    instance = test_helpers.create_cost_changeorder()
    url = reverse("cost_changeorder_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_changeorder_update_view():
    tickets = test_helpers.create_cost_ticket()
    contract = test_helpers.create_cost_contracts()
    client = Client()
    instance = test_helpers.create_cost_changeorder()
    url = reverse("cost_changeorder_update", args=[instance.pk, ])
    data = {
        "backup": http://127.0.0.1,
        "total_labor": "text",
        "status": "text",
        "exclusion_assumption": "text",
        "total_material": "text",
        "total_equipment": "text",
        "change_amt": 1.0f,
        "work_scope": "text",
        "tickets": tickets.pk,
        "contract": contract.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_ticket_list_view():
    instance1 = test_helpers.create_cost_ticket()
    instance2 = test_helpers.create_cost_ticket()
    client = Client()
    url = reverse("cost_ticket_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_ticket_create_view():
    labor_rate = test_helpers.create_project_laborrates()
    material_rate = test_helpers.create_project_materialrates()
    changeorder = test_helpers.create_cost_changeorder()
    equipent_rate = test_helpers.create_project_equipmentrates()
    client = Client()
    url = reverse("cost_ticket_create")
    data = {
        "total_cost": 1.0f,
        "work_start": datetime.now(),
        "status": "text",
        "work_shifts": 1,
        "total_material": 1.0f,
        "work_end": datetime.now(),
        "co_type": "text",
        "total_labor": 1.0f,
        "co_reason": "text",
        "labor_rate": labor_rate.pk,
        "material_rate": material_rate.pk,
        "changeorder": changeorder.pk,
        "equipent_rate": equipent_rate.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_ticket_detail_view():
    client = Client()
    instance = test_helpers.create_cost_ticket()
    url = reverse("cost_ticket_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_ticket_update_view():
    labor_rate = test_helpers.create_project_laborrates()
    material_rate = test_helpers.create_project_materialrates()
    changeorder = test_helpers.create_cost_changeorder()
    equipent_rate = test_helpers.create_project_equipmentrates()
    client = Client()
    instance = test_helpers.create_cost_ticket()
    url = reverse("cost_ticket_update", args=[instance.pk, ])
    data = {
        "total_cost": 1.0f,
        "work_start": datetime.now(),
        "status": "text",
        "work_shifts": 1,
        "total_material": 1.0f,
        "work_end": datetime.now(),
        "co_type": "text",
        "total_labor": 1.0f,
        "co_reason": "text",
        "labor_rate": labor_rate.pk,
        "material_rate": material_rate.pk,
        "changeorder": changeorder.pk,
        "equipent_rate": equipent_rate.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_contracts_list_view():
    instance1 = test_helpers.create_cost_contracts()
    instance2 = test_helpers.create_cost_contracts()
    client = Client()
    url = reverse("cost_contracts_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_contracts_create_view():
    project = test_helpers.create_project_projects()
    company = test_helpers.create_project_company()
    client = Client()
    url = reverse("cost_contracts_create")
    data = {
        "contract_description": "text",
        "attachment": http://127.0.0.1,
        "contract_file": "aFile",
        "scheduleofvalues": "text",
        "contract_type": "text",
        "exclusion_assumption": "text",
        "project": project.pk,
        "company": company.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_contracts_detail_view():
    client = Client()
    instance = test_helpers.create_cost_contracts()
    url = reverse("cost_contracts_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_contracts_update_view():
    project = test_helpers.create_project_projects()
    company = test_helpers.create_project_company()
    client = Client()
    instance = test_helpers.create_cost_contracts()
    url = reverse("cost_contracts_update", args=[instance.pk, ])
    data = {
        "contract_description": "text",
        "attachment": http://127.0.0.1,
        "contract_file": "aFile",
        "scheduleofvalues": "text",
        "contract_type": "text",
        "exclusion_assumption": "text",
        "project": project.pk,
        "company": company.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_requisition_list_view():
    instance1 = test_helpers.create_cost_requisition()
    instance2 = test_helpers.create_cost_requisition()
    client = Client()
    url = reverse("cost_requisition_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_requisition_create_view():
    company = test_helpers.create_project_company()
    project = test_helpers.create_project_projects()
    client = Client()
    url = reverse("cost_requisition_create")
    data = {
        "req_number": "text",
        "req_amount": "text",
        "coi": http://127.0.0.1,
        "stored_materials": 1.0f,
        "prev_amount": 1.0f,
        "lienwaiver": http://127.0.0.1,
        "company": company.pk,
        "project": project.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_requisition_detail_view():
    client = Client()
    instance = test_helpers.create_cost_requisition()
    url = reverse("cost_requisition_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_requisition_update_view():
    company = test_helpers.create_project_company()
    project = test_helpers.create_project_projects()
    client = Client()
    instance = test_helpers.create_cost_requisition()
    url = reverse("cost_requisition_update", args=[instance.pk, ])
    data = {
        "req_number": "text",
        "req_amount": "text",
        "coi": http://127.0.0.1,
        "stored_materials": 1.0f,
        "prev_amount": 1.0f,
        "lienwaiver": http://127.0.0.1,
        "company": company.pk,
        "project": project.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_budget_list_view():
    instance1 = test_helpers.create_cost_budget()
    instance2 = test_helpers.create_cost_budget()
    client = Client()
    url = reverse("cost_budget_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_budget_create_view():
    project = test_helpers.create_project_projects()
    client = Client()
    url = reverse("cost_budget_create")
    data = {
        "line_code": "text",
        "line_amount": "text",
        "line_description": "text",
        "project": project.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_budget_detail_view():
    client = Client()
    instance = test_helpers.create_cost_budget()
    url = reverse("cost_budget_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_budget_update_view():
    project = test_helpers.create_project_projects()
    client = Client()
    instance = test_helpers.create_cost_budget()
    url = reverse("cost_budget_update", args=[instance.pk, ])
    data = {
        "line_code": "text",
        "line_amount": "text",
        "line_description": "text",
        "project": project.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302

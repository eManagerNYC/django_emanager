import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_schedule_list_view():
    instance1 = test_helpers.create_schedule_schedule()
    instance2 = test_helpers.create_schedule_schedule()
    client = Client()
    url = reverse("schedule_schedule_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_schedule_create_view():
    tasks = test_helpers.create_schedule_task()
    client = Client()
    url = reverse("schedule_schedule_create")
    data = {
        "schedule_name": "text",
        "tasks": tasks.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_schedule_detail_view():
    client = Client()
    instance = test_helpers.create_schedule_schedule()
    url = reverse("schedule_schedule_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_schedule_update_view():
    tasks = test_helpers.create_schedule_task()
    client = Client()
    instance = test_helpers.create_schedule_schedule()
    url = reverse("schedule_schedule_update", args=[instance.pk, ])
    data = {
        "schedule_name": "text",
        "tasks": tasks.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_task_list_view():
    instance1 = test_helpers.create_schedule_task()
    instance2 = test_helpers.create_schedule_task()
    client = Client()
    url = reverse("schedule_task_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_task_create_view():
    predecessors = test_helpers.create_schedule_task()
    successors = test_helpers.create_schedule_task()
    client = Client()
    url = reverse("schedule_task_create")
    data = {
        "estimated_end": datetime.now(),
        "actual_start": datetime.now(),
        "task_name": "text",
        "task_duration": 1,
        "actual_end": datetime.now(),
        "estimated_start": datetime.now(),
        "predecessors": predecessors.pk,
        "successors": successors.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_task_detail_view():
    client = Client()
    instance = test_helpers.create_schedule_task()
    url = reverse("schedule_task_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_task_update_view():
    predecessors = test_helpers.create_schedule_task()
    successors = test_helpers.create_schedule_task()
    client = Client()
    instance = test_helpers.create_schedule_task()
    url = reverse("schedule_task_update", args=[instance.pk, ])
    data = {
        "estimated_end": datetime.now(),
        "actual_start": datetime.now(),
        "task_name": "text",
        "task_duration": 1,
        "actual_end": datetime.now(),
        "estimated_start": datetime.now(),
        "predecessors": predecessors.pk,
        "successors": successors.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302

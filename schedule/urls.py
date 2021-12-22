from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("schedule", api.scheduleViewSet)
router.register("task", api.taskViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("schedule/schedule/", views.scheduleListView.as_view(), name="schedule_schedule_list"),
    path("schedule/schedule/create/", views.scheduleCreateView.as_view(), name="schedule_schedule_create"),
    path("schedule/schedule/detail/<int:pk>/", views.scheduleDetailView.as_view(), name="schedule_schedule_detail"),
    path("schedule/schedule/update/<int:pk>/", views.scheduleUpdateView.as_view(), name="schedule_schedule_update"),
    path("schedule/schedule/delete/<int:pk>/", views.scheduleDeleteView.as_view(), name="schedule_schedule_delete"),
    path("schedule/task/", views.taskListView.as_view(), name="schedule_task_list"),
    path("schedule/task/create/", views.taskCreateView.as_view(), name="schedule_task_create"),
    path("schedule/task/detail/<int:pk>/", views.taskDetailView.as_view(), name="schedule_task_detail"),
    path("schedule/task/update/<int:pk>/", views.taskUpdateView.as_view(), name="schedule_task_update"),
    path("schedule/task/delete/<int:pk>/", views.taskDeleteView.as_view(), name="schedule_task_delete"),
)

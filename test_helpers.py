import random
import string

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime

from cost import models as cost_models
from reports import models as reports_models
from schedule import models as schedule_models
from field import models as field_models
from engineering import models as engineering_models
from users import models as users_models
from project import models as project_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_cost_changeorder(**kwargs):
    defaults = {}
    defaults["backup"] = ""
    defaults["total_labor"] = ""
    defaults["status"] = ""
    defaults["exclusion_assumption"] = ""
    defaults["total_material"] = ""
    defaults["total_equipment"] = ""
    defaults["change_amt"] = ""
    defaults["work_scope"] = ""
    if "tickets" not in kwargs:
        defaults["tickets"] = create_cost_ticket()
    if "contract" not in kwargs:
        defaults["contract"] = create_cost_contracts()
    defaults.update(**kwargs)
    return cost_models.changeorder.objects.create(**defaults)
def create_cost_ticket(**kwargs):
    defaults = {}
    defaults["total_cost"] = ""
    defaults["work_start"] = datetime.now()
    defaults["status"] = ""
    defaults["work_shifts"] = ""
    defaults["total_material"] = ""
    defaults["work_end"] = datetime.now()
    defaults["co_type"] = ""
    defaults["total_labor"] = ""
    defaults["co_reason"] = ""
    if "labor_rate" not in kwargs:
        defaults["labor_rate"] = create_project_laborrates()
    if "material_rate" not in kwargs:
        defaults["material_rate"] = create_project_materialrates()
    if "changeorder" not in kwargs:
        defaults["changeorder"] = create_cost_changeorder()
    if "equipent_rate" not in kwargs:
        defaults["equipent_rate"] = create_project_equipmentrates()
    defaults.update(**kwargs)
    return cost_models.ticket.objects.create(**defaults)
def create_cost_contracts(**kwargs):
    defaults = {}
    defaults["contract_description"] = ""
    defaults["attachment"] = ""
    defaults["contract_file"] = ""
    defaults["scheduleofvalues"] = ""
    defaults["contract_type"] = ""
    defaults["exclusion_assumption"] = ""
    if "project" not in kwargs:
        defaults["project"] = create_project_projects()
    if "company" not in kwargs:
        defaults["company"] = create_project_company()
    defaults.update(**kwargs)
    return cost_models.contracts.objects.create(**defaults)
def create_cost_requisition(**kwargs):
    defaults = {}
    defaults["req_number"] = ""
    defaults["req_amount"] = ""
    defaults["coi"] = ""
    defaults["stored_materials"] = ""
    defaults["prev_amount"] = ""
    defaults["lienwaiver"] = ""
    if "company" not in kwargs:
        defaults["company"] = create_project_company()
    if "project" not in kwargs:
        defaults["project"] = create_project_projects()
    defaults.update(**kwargs)
    return cost_models.requisition.objects.create(**defaults)
def create_cost_budget(**kwargs):
    defaults = {}
    defaults["line_code"] = ""
    defaults["line_amount"] = ""
    defaults["line_description"] = ""
    if "project" not in kwargs:
        defaults["project"] = create_project_projects()
    defaults.update(**kwargs)
    return cost_models.budget.objects.create(**defaults)
def create_reports_reports(**kwargs):
    defaults = {}
    defaults["report_name"] = ""
    defaults.update(**kwargs)
    return reports_models.reports.objects.create(**defaults)
def create_schedule_schedule(**kwargs):
    defaults = {}
    defaults["schedule_name"] = ""
    if "tasks" not in kwargs:
        defaults["tasks"] = create_schedule_task()
    defaults.update(**kwargs)
    return schedule_models.schedule.objects.create(**defaults)
def create_schedule_task(**kwargs):
    defaults = {}
    defaults["estimated_end"] = datetime.now()
    defaults["actual_start"] = datetime.now()
    defaults["task_name"] = ""
    defaults["task_duration"] = ""
    defaults["actual_end"] = datetime.now()
    defaults["estimated_start"] = datetime.now()
    if "predecessors" not in kwargs:
        defaults["predecessors"] = create_schedule_task()
    if "successors" not in kwargs:
        defaults["successors"] = create_schedule_task()
    defaults.update(**kwargs)
    return schedule_models.task.objects.create(**defaults)
def create_field_dailyreport(**kwargs):
    defaults = {}
    defaults["report_date"] = datetime.now()
    defaults.update(**kwargs)
    return field_models.dailyreport.objects.create(**defaults)
def create_field_punchlist(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return field_models.punchlist.objects.create(**defaults)
def create_field_checklists(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return field_models.checklists.objects.create(**defaults)
def create_engineering_submittal_pkg(**kwargs):
    defaults = {}
    defaults["package_number"] = ""
    if "submittals" not in kwargs:
        defaults["submittals"] = create_engineering_submittal()
    defaults.update(**kwargs)
    return engineering_models.submittal_pkg.objects.create(**defaults)
def create_engineering_rfi(**kwargs):
    defaults = {}
    defaults["status"] = ""
    defaults["rfi_question"] = ""
    defaults["duedate"] = datetime.now()
    defaults["rfi_number"] = ""
    defaults["rfi_answer"] = ""
    if "rfi_co" not in kwargs:
        defaults["rfi_co"] = create_cost_changeorder()
    if "division" not in kwargs:
        defaults["division"] = create_project_divisions()
    defaults.update(**kwargs)
    return engineering_models.rfi.objects.create(**defaults)
def create_engineering_submittal(**kwargs):
    defaults = {}
    defaults["status"] = ""
    defaults["submittal_file"] = ""
    defaults["submittal_name"] = ""
    defaults["duedate"] = datetime.now()
    defaults["submittal_number"] = ""
    if "division" not in kwargs:
        defaults["division"] = create_project_divisions()
    defaults.update(**kwargs)
    return engineering_models.submittal.objects.create(**defaults)
def create_users_users(**kwargs):
    defaults = {}
    defaults["useremail"] = ""
    defaults["username"] = ""
    defaults["password"] = ""
    defaults.update(**kwargs)
    return users_models.users.objects.create(**defaults)
def create_users_roles(**kwargs):
    defaults = {}
    defaults["rolename"] = ""
    defaults.update(**kwargs)
    return users_models.roles.objects.create(**defaults)
def create_project_company(**kwargs):
    defaults = {}
    defaults["company_address"] = ""
    defaults["company_name"] = ""
    defaults["company_phone"] = ""
    if "division" not in kwargs:
        defaults["division"] = create_project_Divisions()
    defaults.update(**kwargs)
    return project_models.company.objects.create(**defaults)
def create_project_projects(**kwargs):
    defaults = {}
    defaults["project_name"] = ""
    defaults.update(**kwargs)
    return project_models.projects.objects.create(**defaults)
def create_project_reports(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return project_models.reports.objects.create(**defaults)
def create_project_laborrates(**kwargs):
    defaults = {}
    defaults["labor_cost"] = ""
    defaults["labor_affiliation"] = ""
    defaults["labor_name"] = ""
    if "company" not in kwargs:
        defaults["company"] = create_project_company()
    defaults.update(**kwargs)
    return project_models.laborrates.objects.create(**defaults)
def create_project_materialrates(**kwargs):
    defaults = {}
    defaults["material_name"] = ""
    defaults["material_cost"] = ""
    if "company" not in kwargs:
        defaults["company"] = create_project_company()
    defaults.update(**kwargs)
    return project_models.materialrates.objects.create(**defaults)
def create_project_equipmentrates(**kwargs):
    defaults = {}
    defaults["equipment_cost"] = ""
    defaults["equipment_name"] = ""
    defaults.update(**kwargs)
    return project_models.equipmentrates.objects.create(**defaults)
def create_project_divisions(**kwargs):
    defaults = {}
    defaults["division_code"] = ""
    defaults["division_name"] = ""
    defaults.update(**kwargs)
    return project_models.divisions.objects.create(**defaults)

import pytest
import datetime
from freezegun import freeze_time
from project_management_portal.models import User, Project, State, Transition, WorkflowType
from project_management_portal.interactors.storages.dtos import \
    ProjectDto, UserDto, WorkflowTypeDto, ListOfProjectsDto, TaskDto, ListOfTaskssDto



@pytest.fixture()
def users():
    list_of_users = [
        User(username="user1",password="user1passowrd", is_admin=True),
        User(username="user2",password="user2passowrd", is_admin=False),
        User(username="user3",password="user3passowrd", is_admin=False)
        ]
    User.objects.bulk_create(list_of_users)
    users = User.objects.all()
    return users

@pytest.fixture()
def user_dto():
    # user_dto = UserDto(name="user1", user_id=1)
    user_dto = UserDto(
        user_id=1,
        name="Mouli",
        profile_pic="asdfghjk.jpg",
        is_admin=True
    )
    return user_dto


@pytest.fixture()
def workflow_type_dto():
    workflow_type_dto = WorkflowTypeDto(name="wk1", workflow_type_id=1)
    return workflow_type_dto


@pytest.fixture()
@freeze_time("2020-05-29")
def project_dto(user_dto):
    project_details_dto = ProjectDto(
        name='fb',
        description="SocialApp",
        workflow_type=workflow_type_dto,
        created_by=user_dto,
        created_at=datetime.datetime(2020, 5, 29, 0, 0),
        user_id=1,
        project_id=1,
        project_type="CRM"
    )
    return project_details_dto

@pytest.fixture()
@freeze_time("2020-05-29")
def task_dto(project_dto, user_dto):
    task_details_dto = TaskDto(
        title= "",
        task_id=1,
        description="",
        state_id=1,
        issue_type="",
        assigned_to=UserDto,
        project_id=8
    )
    return task_details_dto

@pytest.fixture()
def create_project_expected_output():
    create_project_expected_output = {
        "project_id": 1,
        # "name": "fb",
        "description": "SocialApp",
        "project_type": "CRM",
        # "user": "string",
        "created_at": "2020-05-29 00:00:00",
        "created_by":{
            "user_id":1,
            "name": "Mouli",
            "profile_pic": "asdfghjk.jpg",
            "is_admin": True
        }
    }
    return create_project_expected_output

@pytest.fixture()
@freeze_time("2020-05-29")
def list_of_project_dtos(user_dto, workflow_type_dto):
    list_of_project_dtos = [
        ProjectDto(
        name='ig',
        description='App',
        workflow_type=workflow_type_dto,
        project_type="CRM",
        user_id=user_dto,
        created_at=datetime.datetime(2020, 5, 29, 0, 0),
        project_id=1,
        created_by=user_dto
        )
    ]
    return list_of_project_dtos


@pytest.fixture()
def get_projects_expected_output():
    get_projects_expected_output = [
        {
        "project_id":1,
        "description": "App",
        "project_type": "CRM",
        "created_by": {'is_admin': True,
                           'name': 'Mouli',
                           'profile_pic': 'asdfghjk.jpg',
                           'user_id': 1},
        "created_at": "2020-05-29 00:00:00"
        }
    ]
    return get_projects_expected_output

@pytest.fixture()
def list_of_projects_dto(list_of_project_dtos):
    list_of_project_dto = ListOfProjectsDto(projects_dto=list_of_project_dtos)
    return list_of_project_dto



@pytest.fixture()
def create_task_expected_output():
    create_task_expected_output = {
        "task_id":1,
        'description': '',
        'issue_type': '',
        'project_id': 8,
        'state_id': 1,
        'title': '',
        }
    return create_task_expected_output

@pytest.fixture()
@freeze_time("2020-05-29")
def list_of_task_dtos(user_dto):
    list_of_task_dtos = [
        TaskDto(
        title='ig',
        description='App',
        state_id=1,
        issue_type='Task',
        assigned_to=user_dto,
        project_id=1,
        task_id=1
        )
    ]
    return list_of_task_dtos


@pytest.fixture()
def list_of_tasks_dto(list_of_task_dtos):
    list_of_task_dto = ListOfTaskssDto(tasks_dto=list_of_task_dtos)
    return list_of_task_dto


@pytest.fixture()
def get_tasks_expected_output():
    get_tasks_expected_output = [
        {
        "title":'ig',
        "project_id":1,
        "description": "App",
        "issue_type": "Task",
        # "assigned_to": {'is_admin': True,
        #                   'name': 'Mouli',
        #                   'profile_pic': 'asdfghjk.jpg',
        #                   'user_id': 1},
        "state_id": 1,
        "task_id":1
        }
    ]
    return get_tasks_expected_output

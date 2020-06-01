import pytest
import datetime
from freezegun import freeze_time
from django_swagger_utils.drf_server.exceptions import NotFound
from project_management_portal.storages.create_task_storage_implementation \
    import CreateTaskImplementation
from project_management_portal.interactors.create_task_interactor \
    import CreateTaskInteractor
from project_management_portal.presenters.create_task_presenter_implementation \
    import CreateTaskPresenterImplementation
from project_management_portal.models import Task, WorkflowType


@pytest.mark.django_db
@freeze_time("2020-05-26")
def test_create_task_with_valid_details(users,
                                           workflow, create_project):

    # Arrange
    user_id = 1
    title = "Instagram"
    description = "Best social Network App"
    project_type = 1
    issue_type = "Bug"
    new_task_id = 1
    state_id = 1
    assigned_to = 2
    storage = CreateTaskImplementation()

    # Act

    response = storage.create_task(
        title=title,
        description=description,
        issue_type=issue_type,
        project_id=project_type,
        state_id=state_id,
        assigned_to_id=assigned_to
    )
    # Assert
    # assert response.user_id == user_id
    assert response.description == description
    assert response.task_id == new_task_id
    assert response.title == title
    assert response.issue_type == issue_type


import pytest
import datetime
from django_swagger_utils.drf_server.exceptions import NotFound
from project_management_portal.models import User, Project, WorkflowType
from project_management_portal.interactors.storages.dtos import \
    ProjectDto, UserDto, WorkflowTypeDto
from project_management_portal.presenters.create_task_presenter_implementation import \
    CreateTaskPresenterImplementation
from freezegun import freeze_time

@freeze_time("2020-05-29")
def test_create_task_valid_credentials_returns_task_details(
    task_dto,
    create_task_expected_output):

    # Arrange
    presenter = CreateTaskPresenterImplementation()

    # Act
    response = presenter.get_create_task_response(
        task_dto
    )

    # Assert
    assert response == create_task_expected_output


def test_create_task_with_invalid_assigned_to_id_raises_exception():

    # Arrange
    presenter = CreateTaskPresenterImplementation()
    error_message = "Invalid assigned_to_id"

    # Act
    with pytest.raises(NotFound) as error:
            presenter.raise_exception_for_invalid_assigned_id()

    assert str(error.value) == error_message

def test_create_task_with_invalid_project_id_raises_exception():

    # Arrange
    presenter = CreateTaskPresenterImplementation()
    error_message = "Invalid project_id"

    # Act
    with pytest.raises(NotFound) as error:
            presenter.raise_exception_for_invalid_project_id()

    assert str(error.value) == error_message

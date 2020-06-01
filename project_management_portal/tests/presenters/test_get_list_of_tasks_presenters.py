import pytest
import datetime
from django_swagger_utils.drf_server.exceptions import NotFound
from project_management_portal.models import User, Project, WorkflowType
from project_management_portal.interactors.storages.dtos import \
    ProjectDto, UserDto, WorkflowTypeDto
from project_management_portal.presenters.get_list_of_tasks_presenter_implementation import \
    GetListOfTaskstPresenterImplementation


def test_get_tasks_returns_list_of_tasks(
                list_of_tasks_dto,
                get_tasks_expected_output):

    # Arrange
    presenter = GetListOfTaskstPresenterImplementation()

    # Act
    response = presenter.get_list_of_task_response(
        list_of_tasks_dto
    )

    # Assert
    assert response == get_tasks_expected_output

def test_get_task_with_invalid_project_id_raises_exception():

    # Arrange

    presenter = GetListOfTaskstPresenterImplementation()
    error_message = "Invalid project_id"

    # Act
    with pytest.raises(NotFound) as error:
            presenter.raise_exception_for_invalid_project_id()

    assert str(error.value) == error_message
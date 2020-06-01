import pytest
import datetime
from django_swagger_utils.drf_server.exceptions import NotFound
from project_management_portal.models import User, Project, WorkflowType
from project_management_portal.interactors.storages.dtos import \
    ProjectDto, UserDto, WorkflowTypeDto
from project_management_portal.presenters.get_list_of_projects_presenter_implementation import \
    GetListOfProjectPresenterImplementation


def test_get_projects_returns_list_of_projects(
                list_of_projects_dto,
                get_projects_expected_output):

    # Arrange
    presenter = GetListOfProjectPresenterImplementation()

    # Act
    response = presenter.get_list_of_project_response(
        list_of_projects_dto
    )

    # Assert
    assert response == get_projects_expected_output

def test_get_project_with_invalid_project_type_raises_exception():

    # Arrange
    user_id = 1000
    presenter = GetListOfProjectPresenterImplementation()
    error_message = "Invalid user is not valid"

    # Act
    with pytest.raises(NotFound) as error:
            presenter.raise_exception_for_invalid_user_id(user_id)

    assert str(error.value) == error_message
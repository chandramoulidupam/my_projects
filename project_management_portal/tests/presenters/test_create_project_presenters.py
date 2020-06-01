import pytest
import datetime
from django_swagger_utils.drf_server.exceptions import NotFound
from project_management_portal.models import User, Project, WorkflowType
from project_management_portal.interactors.storages.dtos import \
    ProjectDto, UserDto, WorkflowTypeDto
from project_management_portal.presenters.create_project_presenter_implementation import \
    CreateProjectPresenterImplementation
from freezegun import freeze_time

@pytest.mark.django_db
@freeze_time("2020-05-29")
def test_create_project_valid_credentials_returns_project_details(
                                                project_dto,
                                                create_project_expected_output
                                            ):

    presenter = CreateProjectPresenterImplementation()

    # Act
    response = presenter.get_create_project_response(
        project_dto
    )

    # Assert
    assert response == create_project_expected_output


def test_create_project_with_invalid_workflow_type_raises_exception():

    # Arrange
    presenter = CreateProjectPresenterImplementation()
    error_message = "Invalid workflowtypeError"

    # Act
    with pytest.raises(NotFound) as error:
            presenter.raise_exception_for_invalid_workflow_type()

    assert str(error.value) == error_message


def test_create_project_with_invalid_project_type_raises_exception():

    # Arrange
    presenter = CreateProjectPresenterImplementation()
    error_message = "Invalid user to create project"

    # Act
    with pytest.raises(NotFound) as error:
            presenter.raise_exception_for_user_is_not_admin()

    assert str(error.value) == error_message
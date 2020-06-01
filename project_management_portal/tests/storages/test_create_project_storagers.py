import pytest
import datetime
from freezegun import freeze_time
from django_swagger_utils.drf_server.exceptions import NotFound
from project_management_portal.storages.create_project_storage_implementation \
    import CreateProjectImplementation
from project_management_portal.interactors.create_project_interactor \
    import CreateProjectInteractor
from project_management_portal.presenters.create_project_presenter_implementation \
    import CreateProjectPresenterImplementation
from project_management_portal.models import Project, WorkflowType


@pytest.mark.django_db
@freeze_time("2020-05-26")
def test_create_project_with_valid_details(users,
                                           workflow):

    # Arrange
    user_id = 1
    name = "Instagram"
    description = "Best social Network App"
    workflow_type = 1
    project_type = "CRM"
    created_at = datetime.datetime(2020, 5, 26, 0, 0)
    storage = CreateProjectImplementation()
    workflow_type_obj = WorkflowType.objects.get(id=workflow_type)

    # Act

    response = storage.create_project(
        name=name,
        description=description,
        workflow_type=workflow_type,
        project_type=project_type,
        user_id=user_id
    )

    # Assert
    assert response.name == name
    assert response.user_id == user_id
    assert response.description == description
    assert response.project_type == project_type
    # assert response.workflow_type == workflow_type_obj
    assert response.created_at == created_at

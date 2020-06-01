import pytest
import datetime
from django_swagger_utils.drf_server.exceptions import NotFound
from project_management_portal.storages.get_list_of_projects_storage_implementation \
    import GetListOfProjectImplementation
from project_management_portal.interactors.create_project_interactor \
    import CreateProjectInteractor
from project_management_portal.presenters.create_project_presenter_implementation \
    import CreateProjectPresenterImplementation
from project_management_portal.models import Project, WorkflowType
from project_management_portal.interactors.storages.dtos import \
    WorkflowTypeDto, UserDto, ProjectDto


# @pytest.mark.django_db
# def test_get_list_of_projects_with_invalid_user_id_raise_exception():
#     # Arrange
#     user_id = -1
#     storage = GetListOfProjectImplementation()

#     with pytest.raises(NotFound):
#         storage.is_user_valid(user_id=user_id)

@pytest.mark.django_db
def test_get_list_of_projects_for_admin_returns_list_of_projects(users,workflow, transitions, states, create_project):

    # Arrange
    user_id = 1
    offset =0
    limit = 1
    storage = GetListOfProjectImplementation()
    mock_excepted_output = [ProjectDto(user_id=1, project_id=1, name='project_1', description='description1', workflow_type=WorkflowTypeDto(name='workflow1', workflow_type_id=1), project_type='CRM', created_by=UserDto(name='', user_id=1, profile_pic='', is_admin=True), created_at=datetime.datetime(2020, 5, 20, 0, 0))]

    # Act
    response = storage.get_list_of_project_for_admin(
        user_id=user_id,
        offset=offset,
        limit=limit
    )
    # print(response)
    # Assert
    assert response == mock_excepted_output
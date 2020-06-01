import pytest
import datetime
from django_swagger_utils.drf_server.exceptions import NotFound
from project_management_portal.storages.get_list_of_tasks_storage_implementation \
    import GetListOfTaskImplementation
from project_management_portal.interactors.create_project_interactor \
    import CreateProjectInteractor
from project_management_portal.presenters.create_project_presenter_implementation \
    import CreateProjectPresenterImplementation
from project_management_portal.models import Project, WorkflowType
from project_management_portal.interactors.storages.dtos import \
    WorkflowTypeDto, UserDto, ProjectDto, TaskDto

# @pytest.mark.django_db
# def test_get_list_of_projects_with_invalid_user_id_raise_exception():
#     # Arrange
#     user_id = -1
#     storage = GetListOfProjectImplementation()

#     with pytest.raises(NotFound):
#         storage.is_user_valid(id=user_id)

@pytest.mark.django_db
def test_get_list_of_task_for_admin_returns_list_of_projects(users,workflow, transitions, states, create_project,create_task):

    # Arrange
    project_id = 1
    # offset =1
    # limit = 3
    storage = GetListOfTaskImplementation()
    mock_excepted_output = [TaskDto(title='PMP', task_id=1, description='project_management_portal', state_id=1, issue_type='Task', assigned_to={'user_id': 1, 'name': '', 'profile_pic': '', 'is_admin': True}, project_id=1)]

    # Act
    response = storage.get_list_of_tasks_for_user(
        project_id=project_id,
        # offset=offset,
        # limit=limit
    )

    # Assert
    assert response == mock_excepted_output
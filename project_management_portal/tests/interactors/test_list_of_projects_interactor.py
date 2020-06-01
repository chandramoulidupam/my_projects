import pytest
import datetime
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from common.oauth2_storage import OAuth2SQLStorage
from project_management_portal.interactors.get_list_of_projects import \
    GetListOfProjectInteractor
from project_management_portal.interactors.presenters.presenter_interface import \
    PresenterInterface
from project_management_portal.interactors.storages.get_list_of_projects_storage_interface import \
    GetListOfProjectInterface
from project_management_portal.presenters.get_list_of_projects_presenter_implementation import GetListOfProjectPresenterImplementation

@pytest.mark.django_db
class TestGetProjectInteractor:

    def test_get_list_of_project_with_valid_details(self):

        # Arrange
        new_project_id = 1
        name = "project_management_portal"
        offset = 1
        limit = 4
        user_id = 1
        mock_presenter_response = {"project_id": new_project_id}
    
        storage = create_autospec(GetListOfProjectInterface)
        presenter = create_autospec(PresenterInterface)
    
        interactor = GetListOfProjectInteractor(
            storage=storage,
            presenter=presenter
        )
    
        storage.get_list_of_project_for_admin.return_value = new_project_id
        presenter.get_list_of_project_response. \
            return_value = mock_presenter_response
    
        # Act
        response = interactor.get_list_of_project(
            user_id=user_id,
            offset=offset,
            limit=limit
        )
    
        # Assert
        storage.get_list_of_project_for_admin.assert_called_once_with(
            user_id=user_id,
            offset=offset,
            limit=limit
        )
    
        presenter.get_list_of_project_response.assert_called_once_with(
            project_id=new_project_id
        )

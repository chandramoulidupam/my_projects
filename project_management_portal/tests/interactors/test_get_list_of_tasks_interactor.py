import pytest
import datetime
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from common.oauth2_storage import OAuth2SQLStorage
from project_management_portal.interactors.get_list_of_tasks import \
    GetListOfTaskInteractor
from project_management_portal.interactors.presenters.presenter_interface import \
    PresenterInterface
from project_management_portal.interactors.storages.get_list_of_tasks_storage_interface import \
    GetListOfTaskInterface
from project_management_portal.presenters.get_list_of_tasks_presenter_implementation import GetListOfTaskstPresenterImplementation

@pytest.mark.django_db
class TestGetTaskInteractor:

    def test_get_list_of_tasks_with_valid_details(self):

        # Arrange
        new_task_id = 1
        # name = "project_management_portal"
        offset = 1
        limit = 4
        project_id = 2
        mock_presenter_response = {"task_id": new_task_id}
    
        storage = create_autospec(GetListOfTaskInterface)
        presenter = create_autospec(PresenterInterface)
    
        interactor = GetListOfTaskInteractor(
            storage=storage,
            presenter=presenter
        )
    
        storage.get_list_of_tasks_for_user.return_value = new_task_id
        presenter.get_list_of_task_response. \
            return_value = mock_presenter_response
    
       #  Act
        response = interactor.get_list_of_tasks_for_user(
            project_id=project_id,
        )

        # Assert
        storage.get_list_of_tasks_for_user.assert_called_once_with(
            project_id
        )

        presenter.get_list_of_task_response.assert_called_once_with(
            new_task_id
        )


    def test_is_valid_project_id_given_invalid_project_id_returns_false(self):

        # Arrange
        project_id = 100000
        storage = create_autospec(GetListOfTaskInterface)
        presenter = create_autospec(PresenterInterface)
        storage.is_project_id_valid.return_value = False
        presenter.raise_exception_for_invalid_project_id.side_effect = NotFound

        interactor = GetListOfTaskInteractor(
            storage=storage,
            presenter=presenter
        )

        # Act
        with pytest.raises(NotFound):
            response = interactor.get_list_of_tasks_for_user(
                project_id=project_id
            )

        # Assert
        presenter.raise_exception_for_invalid_project_id.assert_called_once()


import pytest
import datetime
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from common.oauth2_storage import OAuth2SQLStorage
from project_management_portal.interactors.update_state_interactor import \
    StateUpdateInteractor
from project_management_portal.interactors.presenters.presenter_interface import \
    PresenterInterface
from project_management_portal.interactors.storages.update_state_storage_interactor import \
    StateUpdateStorageInterface


@pytest.mark.django_db
class TestTaskProjectInteractor:

    def test_state_update_with_valid_details_return_create_transition(self):

        # Arrange
        name = "TODO"
        # description = "Social Network"
        task_id = 1
        project_id = 1
        to_state_id = 2
        
        storage = create_autospec(StateUpdateStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = StateUpdateInteractor(
            storage=storage,
            presenter=presenter
        )
        # storage.create_task.return_value = new_task_id
        # presenter.get_create_project_response. \
        #     return_value = mock_presenter_response
    
        # Act
        response = interactor.state_update(
                name=name,
                project_id=project_id,
                task_id=task_id,
                to_state_id=to_state_id
            )
    
        # Assert
        storage.state_update.assert_called_once_with(
            name=name,
            to_state_id=to_state_id,
            project_id=project_id,
            task_id=task_id
        )


    def test_state_update_with_invalid_project_id_raises_exception(self):

        # Arrange
        name = "TODO"
        # description = "Social Network"
        task_id = 1
        project_id = 100
        to_state_id = 2
        storage = create_autospec(StateUpdateStorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.valid_project_id.return_value = False
        presenter.raise_exception_for_invalid_project_id.side_effect = NotFound

        interactor = StateUpdateInteractor(
            storage=storage,
            presenter=presenter
        )

        # Act
        with pytest.raises(NotFound):
            response = interactor.state_update(
                name=name,
                project_id=project_id,
                task_id=task_id,
                to_state_id=to_state_id
            )

        # Assert
        presenter.raise_exception_for_invalid_project_id.assert_called_once()

    def test_update_state_when_task_id_is_invalid_raises_exception(self):

        # Arrange
        name = "TODO"
        # description = "Social Network"
        task_id = 1000
        project_id = 1
        to_state_id = 2
        storage = create_autospec(StateUpdateStorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.valid_task_id.return_value = False
        presenter.raise_exception_for_invalid_task_id.side_effect = NotFound

        interactor = StateUpdateInteractor(
            storage=storage,
            presenter=presenter
        )

        # Act
        with pytest.raises(NotFound):
            response = interactor.state_update(
                name=name,
                project_id=project_id,
                task_id=task_id,
                to_state_id=to_state_id
            )

        # Assert
        presenter.raise_exception_for_invalid_task_id.assert_called_once()

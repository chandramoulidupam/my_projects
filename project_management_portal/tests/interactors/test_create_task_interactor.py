import pytest
import datetime
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from common.oauth2_storage import OAuth2SQLStorage
from project_management_portal.interactors.create_task_interactor import \
    CreateTaskInteractor
from project_management_portal.interactors.presenters.presenter_interface import \
    PresenterInterface
from project_management_portal.interactors.storages.create_task_storage_interface import \
    TaskStorageInterface
from project_management_portal.presenters.create_task_presenter_implementation import \
    CreateTaskPresenterImplementation

@pytest.mark.django_db
class TestTaskProjectInteractor:

    def test_create_task_with_valid_details_return_task_id(self):

        # Arrange
        title = "Ig"
        description = "Social Network"
        issue_type = "Task"
        project_id = 1
        new_task_id = 1
        assigned_to = 1
        state_id = 1
        mock_presenter_response = {"task_id": new_task_id}
        storage = create_autospec(TaskStorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = CreateTaskInteractor(
            storage=storage,
            presenter=presenter
        )
        storage.create_task.return_value = new_task_id
        presenter.get_create_project_response. \
            return_value = mock_presenter_response
    
        # Act
        response = interactor.create_task(
                title=title,
                project_id=project_id,
                description=description,
                issue_type=issue_type,
                assigned_to_id=assigned_to,
                state_id=state_id
            )
    
        # Assert
        storage.create_task.assert_called_once_with(
            title=title,
            project_id=project_id,
            description=description,
            issue_type=issue_type,
            assigned_to_id=assigned_to,
            state_id=state_id
        )

        presenter.get_create_task_response.assert_called_once_with(
            new_task_id
        )

    def test_create_task_with_invalid_project_id_raises_exception(self):

        # Arrange
        title = "Ig"
        description = "Social Network"
        issue_type = "Task"
        project_id = 100000
        assigned_to = 1
        state_id = 1
        storage = create_autospec(TaskStorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.is_project_id_valid.return_value = False
        presenter.raise_exception_for_invalid_project_id.side_effect = NotFound

        interactor = CreateTaskInteractor(
            storage=storage,
            presenter=presenter
        )

        # Act
        with pytest.raises(NotFound):
            response = interactor.create_task(
                title=title,
                project_id=project_id,
                description=description,
                issue_type=issue_type,
                assigned_to_id=assigned_to,
                state_id=state_id
            )

        # Assert
        presenter.raise_exception_for_invalid_project_id.assert_called_once()

    def test_create_task_when_assigned_to_id_is_invalid_raises_exception(self):

        # Arrange
        title = "Ig"
        description = "Social Network"
        issue_type = "Task"
        project_id = 1
        assigned_to = 1000000
        state_id = 1
        storage = create_autospec(TaskStorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.is_assigned_to_id_valid.return_value = False
        presenter.raise_exception_for_invalid_assigned_id.side_effect = NotFound

        interactor = CreateTaskInteractor(
            storage=storage,
            presenter=presenter
        )

        # Act
        with pytest.raises(NotFound):
            response = interactor.create_task(
                title=title,
                project_id=project_id,
                description=description,
                issue_type=issue_type,
                assigned_to_id=assigned_to,
                state_id=state_id
            )

        # Assert
        presenter.raise_exception_for_invalid_assigned_id.assert_called_once()

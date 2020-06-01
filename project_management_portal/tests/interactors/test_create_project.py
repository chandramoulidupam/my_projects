import pytest
import datetime
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from common.oauth2_storage import OAuth2SQLStorage
from project_management_portal.interactors.create_project_interactor import \
    CreateProjectInteractor
from project_management_portal.interactors.presenters.presenter_interface import \
    PresenterInterface
from project_management_portal.interactors.storages.create_project_storage_interface import \
    ProjectStorageInterface
from project_management_portal.presenters.create_project_presenter_implementation import CreateProjectPresenterImplementation

@pytest.mark.django_db
class TestCreateProjectInteractor:

    def test_create_project_with_invalid_workflow_type_raises_exception(self):

        # Arrange
        name = "Ig"
        description = "Social Network"
        workflow_type = -1
        user_id = 1
        project_type = "CRM"
        storage = create_autospec(ProjectStorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.valid_workflow_type.return_value = False
        presenter.raise_exception_for_invalid_workflow_type.side_effect = NotFound

        interactor = CreateProjectInteractor(
            storage=storage,
            presenter=presenter
        )

        # Act
        with pytest.raises(NotFound):
            interactor.create_project(
                name=name,
                user_id=user_id,
                description=description,
                workflow_type=workflow_type,
                project_type=project_type
            )

        # Assert
        presenter.raise_exception_for_invalid_workflow_type.assert_called_once()

    def test_create_project_with_user_is_not_admin_raises_exception(self):

        # Arrange
        name = "Ig"
        description = "Social Network"
        workflow_type = 1
        user_id = 1
        project_type = "CRM"
        storage = create_autospec(ProjectStorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.user_is_not_admin.return_value = False
        presenter.raise_exception_for_user_is_not_admin.side_effect = NotFound

        interactor = CreateProjectInteractor(
            storage=storage,
            presenter=presenter
        )

        # Act
        with pytest.raises(NotFound):
            interactor.create_project(
                name=name,
                user_id=user_id,
                description=description,
                workflow_type=workflow_type,
                project_type=project_type
            )

        # Assert
        presenter.raise_exception_for_user_is_not_admin.assert_called_once()


    def test_create_project_with_valid_details(self):

        # Arrange
        user_id = 1
        new_project_id = 1
        name = "project_management_portal"
        description = "The name of the project is Project Management Portal"
        workflow_type = 1
        project_type = "CRM"
        mock_presenter_response = {"project_id": new_project_id}
    
        storage = create_autospec(ProjectStorageInterface)
        presenter = create_autospec(PresenterInterface)
    
        interactor = CreateProjectInteractor(
            storage=storage,
            presenter=presenter
        )
    
        storage.create_project.return_value = new_project_id
        presenter.get_create_project_response. \
            return_value = mock_presenter_response
    
        # Act
        response = interactor.create_project(
            user_id=user_id,
            name=name,
            description=description,
            workflow_type=workflow_type,
            project_type=project_type
        )
    
        # Assert
        storage.create_project.assert_called_once_with(
            name=name,
            description=description,
            workflow_type=workflow_type,
            project_type=project_type,
            user_id=user_id,
        )
    
        presenter.get_create_project_response.assert_called_once_with(
            project_id=new_project_id
        )
    
        assert response == mock_presenter_response
    

import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from common.oauth2_storage import OAuth2SQLStorage
from project_management_portal.interactors.login_interactor import \
    LoginInteractor
from project_management_portal.interactors.presenters.presenter_interface import \
    PresenterInterface
from project_management_portal.interactors.storages.user_login_storage_interface import \
    UserLoginStorageInterface
from project_management_portal.presenters.user_login_presenter_implementation import UserLoginPresenterImplementation

@pytest.mark.django_db
class TestUserLoginInteractor:

    def test_given_invalid_username_raises_exception(self):

        # Arrange
        username = "mouli"
        password = "lolololo"
        invalid_username = "mouli"
        oauth_storage = OAuth2SQLStorage(
            )
        storage = create_autospec(UserLoginStorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.valid_username.return_value = False
        presenter.raise_exception_for_invalid_username.side_effect = NotFound

        interactor = LoginInteractor(
            storage=storage,
            oauth_storage=oauth_storage,
            presenter=presenter
        )

        # Act
        with pytest.raises(NotFound):
            interactor.user_login(
                username=username,
                password=password,
            )

        # Assert
        storage.valid_username.assert_called_once_with(
            username=invalid_username
        )
        presenter.raise_exception_for_invalid_username.assert_called_once()


    def test_given_invalid_password_raises_exception(self):

        # Arrange
        username = "mouli"
        password = "lololololl"
        oauth_storage = OAuth2SQLStorage(
            )
        storage = create_autospec(UserLoginStorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.valid_password.return_value = False
        presenter.raise_exception_for_invalid_password.side_effect = NotFound

        interactor = LoginInteractor(
            storage=storage,
            oauth_storage=oauth_storage,
            presenter=presenter
        )

        # Act
        with pytest.raises(NotFound):
            interactor.user_login(
                username=username,
                password=password,
            )

        # Assert
        storage.valid_username.assert_called_once_with(
            username=username
        )
        storage.valid_password.assert_called_once_with(
            username=username,
            password=password
        )
        presenter.raise_exception_for_invalid_password.assert_called_once()

    # def test_given_valid_username_and_password_retrurns_tokens(self):

    #     # Arrange
    #     username = "mouli"
    #     password = "lololololl"
    #     oauth_storage = OAuth2SQLStorage(
    #         )
    #     storage = create_autospec(UserLoginStorageInterface)
    #     presenter = create_autospec(PresenterInterface)

    #     interactor = LoginInteractor(
    #         storage=storage,
    #         oauth_storage=oauth_storage,
    #         presenter=presenter
    #     )
    #     mock_response = {
    #         "access_token" : "some_access_token",
    #         "refresh_token": "some_refresh_token"
    #     }

    #     # Act
    #     response = interactor.user_login(username=username,password=password)
 
    #     # Assert
    #     storage.valid_username.assert_called_once_with(
    #         username=username
    #     )
    #     storage.valid_password.assert_called_once_with(
    #         username=username,
    #         password=password
    #     )
    #     presenter.user_login_response.assert_called_once_with(username=username,password=password)
    #     assert response == mock_response

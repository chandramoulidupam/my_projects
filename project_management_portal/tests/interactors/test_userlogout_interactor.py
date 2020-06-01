import pytest
from django_swagger_utils.drf_server.exceptions import NotFound
from unittest.mock import create_autospec
from common.oauth2_storage import OAuth2SQLStorage
from project_management_portal.interactors.logout_interactor import \
    LogoutInteractor
from project_management_portal.interactors.presenters.presenter_interface import \
    PresenterInterface
from project_management_portal.interactors.storages.user_logout_storage_interface import \
    UserLogoutStorageInterface

class TestUserLogoutInteractor:

    def test_given_invalid_access_token_raises_exception(self):

        # Arrange
        access_token="123456"
        storage = create_autospec(UserLogoutStorageInterface)
        presenter = create_autospec(PresenterInterface)
        storage.valid_accesstoken.return_value = False
        presenter.raise_exception_for_invalid_access_token.side_effect = NotFound

        interactor = LogoutInteractor(
            storage=storage,
            presenter=presenter
        )

        # Act
        with pytest.raises(NotFound):
            interactor.user_logout(
                access_token=access_token
            )

        # Assert
        storage.valid_accesstoken.assert_called_once_with(
            access_token=access_token
        )
        presenter.raise_exception_for_invalid_access_token.assert_called_once()

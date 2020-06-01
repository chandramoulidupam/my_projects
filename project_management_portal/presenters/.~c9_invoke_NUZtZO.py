from common.dtos import UserAuthTokensDTO
from project_management_portal.interactors.login_interactor import LoginInteractor
from project_management_portal.interactors.presenters.presenter_interface import PresenterInterface
from project_management_portal.exceptions.exceptions import \
    InvalidPassword, InvalidUsername, InvalidDescription, InvalidAccessToken


class UserLogoutPresenterImplementation(PresenterInterface):
    def raise_exception_for_invalid_access_token(self):
        raise InvalidAccessToken

    def delete_accesstoken(self, token):
        pass

    
















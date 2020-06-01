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

 
    def get_create_project_response(self, project_id: int):
        pass

 
    def raise_invalid_description_exception(self):
        pass

 
    def raise_exception_for_invalid_username(self):
        pass

 
    def raise_exception_for_invalid_password(self):
        pass

 
    def get_acces_token_dto_response(self, token):
        pass

 
    def delete_accesstoken(self, token):
        pass

 
    def raise_exception_for_invalid_access_token(self):
        pass

 
    def get_list_of_project_response(self, project_id):
        pass

 
    def user_login_response(self,username, password):
        pass

 
    def raise_exception_for_invalid_workflow_type_id(self, workflow_type):
        pass

 
    def raise_exception_for_invalid_project_type(self, project_type):
        pass

 
    def raise_exception_for_invalid_project_id(self, project_type):
        pass

 
    def get_create_task_response(self, project_id: int):
        pass

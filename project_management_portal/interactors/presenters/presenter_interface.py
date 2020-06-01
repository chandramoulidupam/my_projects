from abc import ABC
from abc import abstractmethod


class PresenterInterface(ABC):

    @abstractmethod
    def get_create_project_response(self, project_id: int):
        pass

    @abstractmethod
    def raise_invalid_description_exception(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_username(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_password(self):
        pass

    @abstractmethod
    def get_acces_token_dto_response(self, token):
        pass

    @abstractmethod
    def delete_accesstoken(self, token):
        pass

    @abstractmethod
    def raise_exception_for_invalid_access_token(self):
        pass

    @abstractmethod
    def get_list_of_project_response(self, project_id):
        pass

    @abstractmethod
    def user_login_response(self,username, password):
        pass

    @abstractmethod
    def raise_exception_for_invalid_workflow_type(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_project_id(self, project_id):
        pass

    @abstractmethod
    def raise_exception_for_invalid_project_type(self, project_type):
        pass

    @abstractmethod
    def get_create_task_response(self, task_id: int):
        pass

    @abstractmethod
    def get_list_of_task_response(self, task_id: int):
        pass

    @abstractmethod
    def raise_exception_for_invalid_assigned_id(self, user_id: int):
        pass

    @abstractmethod
    def raise_exception_for_user_is_not_admin(self, user_id: int):
        pass

    @abstractmethod
    def raise_exception_for_invalid_user_id(self, user_id: int):
        pass

    @abstractmethod
    def raise_exception_for_invalid_task_id(self, task_id: int):
        pass

    @abstractmethod
    def raise_exception_for_invalid_to_state_id(self, to_state_id: int):
        pass
from common.dtos import UserAuthTokensDTO
from django_swagger_utils.drf_server.exceptions import NotFound
from project_management_portal.interactors.presenters.presenter_interface import PresenterInterface
from project_management_portal.models import Project
from project_management_portal.presenters.create_project_presenter_implementation import CreateProjectPresenterImplementation
USERISNOTVALID=("Invalid user is not valid","USERISNOTVALID")

class GetListOfProjectPresenterImplementation(PresenterInterface):

    def get_list_of_project_response(self, project_obj_dtos):
        project_instance = CreateProjectPresenterImplementation()
        # print("\n"*10, project_obj_dtos)
        list_of_projects = [project_instance.get_create_project_response(project_obj_dto) for project_obj_dto in project_obj_dtos]
        return list_of_projects

 
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


 
    def raise_exception_for_invalid_workflow_type(self):
        pass


    def is_assigned_to_id_valid(self, assigned_to: int):
        pass

    def get_list_of_task_response(self, user_id):
        pass

    def raise_exception_for_invalid_assigned_id(self, user_id: int):
        pass

    def raise_exception_for_user_is_not_admin(self, user_id: int):
        pass

    def raise_exception_for_invalid_user_id(self, user_id: int):
        raise NotFound(*USERISNOTVALID)

    def raise_exception_for_invalid_task_id(self, task_id: int):
        pass

    def raise_exception_for_invalid_to_state_id(self, to_state_id: int):
        pass
from common.dtos import UserAuthTokensDTO
from django_swagger_utils.drf_server.exceptions import NotFound
from project_management_portal.interactors.create_task_interactor import CreateTaskInteractor
from project_management_portal.interactors.presenters.presenter_interface import PresenterInterface
from project_management_portal.exceptions.exceptions import \
    InvalidPassword, InvalidUsername, InvalidDescription, InvalidAccessToken, InvalidWorkflowType, InvalidProjectId, InvalidAssignedToId
from project_management_portal.models import Task
INVALIDPROJECTID=("Invalid project_id","INVALIDPROJECTID")
INVALIDASSIGNEDTOID=("Invalid assigned_to_id","INVALIDASSIGNEDTOID")


class CreateTaskPresenterImplementation(PresenterInterface):

 
    def get_create_task_response(self, task_dto):
        # print("\n"*10,task_dto,"\n"*10)
        # task_dto = Task.objects.get(task_id=task_id)
        response = {
            "task_id": task_dto.task_id,
            "title": task_dto.title,
            "description": task_dto.description,
            "project_id": task_dto.project_id,
            "issue_type": task_dto.issue_type,
            "state_id": task_dto.state_id
        }
        return response

 
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

 
    def raise_exception_for_invalid_workflow_type(self):
        pass

 
    def raise_exception_for_invalid_project_type(self, project_type):
        pass

 
    def raise_exception_for_invalid_project_id(self):
        raise NotFound(*INVALIDPROJECTID)


    def raise_exception_for_invalid_assigned_id(self):
        raise NotFound(*INVALIDASSIGNEDTOID)

    def get_create_project_response(self, project_id: int):
        pass

    def get_list_of_task_response(self, task_id: int):
        pass

    def raise_exception_for_invalid_user_id(self, user_id: int):
        pass

    def raise_exception_for_user_is_not_admin(self, user_id: int):
        pass

    def raise_exception_for_invalid_task_id(self, task_id: int):
        pass

    def raise_exception_for_invalid_to_state_id(self, to_state_id: int):
        pass
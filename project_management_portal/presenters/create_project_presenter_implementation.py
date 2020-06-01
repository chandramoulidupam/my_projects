from common.dtos import UserAuthTokensDTO
from django_swagger_utils.drf_server.exceptions import NotFound
from project_management_portal.interactors.create_project_interactor import CreateProjectInteractor
from project_management_portal.interactors.presenters.presenter_interface import PresenterInterface
from project_management_portal.exceptions.exceptions import \
    InvalidPassword, InvalidUsername, InvalidDescription, InvalidAccessToken, InvalidWorkflowType
from project_management_portal.models import Project, User
from project_management_portal.interactors.storages.dtos import \
    WorkflowTypeDto, UserDto, ProjectDto
WORKFLOWERROR=("Invalid workflowtypeError","WORKFLOWERROR")
USERISNOTADMIN=("Invalid user to create project","USERISNOTADMIN")


class CreateProjectPresenterImplementation(PresenterInterface):
    def raise_invalid_description_exception(self):
        raise InvalidDescription

    def get_create_project_response(self, project_dto):
        # print("\n"*10,project_dto.created_by)
        # project_dto = Project.objects.get(id=project_id)
        # user_obj = User.objects.get(id=project_dto.created_by.id)
        response = {
            
            "description": project_dto.description,
            "project_type": project_dto.project_type,
            "created_at": str(project_dto.created_at),
            "created_by": self._get_user_dto(project_dto.created_by),
            "project_id": project_dto.project_id,
        }
        return response

    def _get_user_dto(self, user_obj):
        
        user_dto = {
            "user_id": user_obj.user_id,
            "name": user_obj.name,
            "profile_pic": user_obj.profile_pic,
            "is_admin": user_obj.is_admin
            }

        return user_dto

    def get_acces_token_dto_response(self, token):
        pass

    def raise_exception_for_invalid_username(self):
        pass

 
    def raise_exception_for_invalid_password(self):
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
        raise NotFound(*WORKFLOWERROR)

 
    def raise_exception_for_invalid_project_type(self, project_type):
        pass

 
    def raise_exception_for_invalid_project_id(self, project_type):
        pass

 
    def get_create_task_response(self, project_id: int):
        pass

    def is_assigned_to_id_valid(self, assigned_to: int):
        pass

    def get_list_of_task_response(self, task_id: int):
        pass

    def raise_exception_for_user_is_not_admin(self):
        raise NotFound(*USERISNOTADMIN)

    def raise_exception_for_invalid_assigned_id(self, user_id: int):
        pass


    def raise_exception_for_invalid_user_id(self, user_id: int):
        pass

    def raise_exception_for_invalid_task_id(self, task_id: int):
        pass

    def raise_exception_for_invalid_to_state_id(self, to_state_id: int):
        pass
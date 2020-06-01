from project_management_portal.interactors.storages.get_list_of_projects_storage_interface import \
    GetListOfProjectInterface
from oauth2_provider.models import AccessToken
# from project_management_portal.interactors.storages.dtos import \
#     UserDto, CommentDto, CommentRepliesDto
from project_management_portal.models import User, Project, WorkflowType
from project_management_portal.interactors.storages.dtos import \
    WorkflowTypeDto, UserDto, ProjectDto


class GetListOfProjectImplementation(GetListOfProjectInterface):


    def get_list_of_project_for_admin(self, user_id: int, offset: int, limit: int):

        project_objs = Project.objects.filter(created_by=user_id)[offset:offset+limit]
        list_of_projects = []
        for project_obj in project_objs:
            user_dtos = self.for_user_dto(project_obj.created_by_id)
            workflow_type_objs = self.for_workflow_dto(project_obj.workflow_type)
            project_dto = self._get_project_details_dto(project_obj, workflow_type_objs, user_dtos, user_id)
            list_of_projects.append(project_dto)
        # list_of_projects = [self._get_project_details_dto(project_obj) for project_obj in project_objs]
        # print("\n"*10,list_of_projects,"\n"*10)
        return list_of_projects

    def get_list_of_project_for_user(self, user_id, offset: int, limit: int):
        project_objs = Project.objects.filter(assigned_to=user_id)[offset:offset+limit]
        list_of_projects = []
        for project_obj in project_objs:
            user_dtos = self.for_user_dto(project_obj.assigned_to_id)
            workflow_type_objs = self.for_workflow_dto(project_obj.workflow_type)
            project_dto = self._get_project_details_dto(project_obj, workflow_type_objs, user_dtos, user_id)
            list_of_projects.append(project_dto)
        # list_of_projects = [self._get_project_details_dto(project_obj) for project_obj in project_objs]

        return list_of_projects


    def for_user_dto(self,user_id):
        user_obj = User.objects.get(id=user_id)
        user_dto = self._get_user_dto(user_obj)
        return user_dto


    def for_workflow_dto(self, workflow_type):
        workflow_type_obj = WorkflowType.objects.get(
            id=workflow_type.id
        )

        workflow_type_dto = self._get_workflow_type_dto(workflow_type_obj)
        return workflow_type_dto


    def _get_project_details_dto(self,
                                 project_obj, workflow_type_obj, user_dto, user_id):

        project_details_dto = ProjectDto(
            name=project_obj.name,
            description=project_obj.description,
            workflow_type=workflow_type_obj,#TODO objectDto
            project_type=project_obj.project_type,
            created_by=user_dto,#TODO object DTO
            created_at=project_obj.created_at,
            project_id=project_obj.id,
            user_id=user_id
        )
        return project_details_dto

    
    def _get_user_dto(self, user_obj):

        user_dto = UserDto(
            name=user_obj.name,
            user_id=user_obj.id,
            profile_pic=user_obj.profile_pic,
            is_admin=user_obj.is_admin
        )

        return user_dto

    def _get_workflow_type_dto(self, workflow_type_obj):

        workflow_type_dto = WorkflowTypeDto(
            name=workflow_type_obj.name,
            workflow_type_id=workflow_type_obj.id
        )

        return workflow_type_dto

    def is_user_valid(self, user_id):
        is_user_exists = User.objects.filter(id=user_id).exists()
        return is_user_exists

    def is_user_admin(self, user_id):
        is_user_admin = Project.objects.filter(created_by=user_id).exists()
        return is_user_admin
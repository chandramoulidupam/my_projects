from project_management_portal.interactors.storages.create_project_storage_interface import \
    ProjectStorageInterface
from oauth2_provider.models import AccessToken
from project_management_portal.models import User, WorkflowType, Project
from project_management_portal.interactors.storages.dtos import \
    WorkflowTypeDto, UserDto, ProjectDto


class CreateProjectImplementation(ProjectStorageInterface):
    def create_project(self, name: str,workflow_type: int, project_type: str,
                               description: str, user_id: int) -> int:
        user_obj = User.objects.get(id=user_id)

        user_dto = self._get_user_dto(user_obj)

        workflow_type_obj = WorkflowType.objects.get(
            id=workflow_type
        )

        workflow_type_dto = self._get_workflow_type_dto(workflow_type_obj)

        project_obj = Project.objects.create(name=name,
                                            description=description,
                                            workflow_type_id=workflow_type,
                                            project_type=project_type,
                                            created_by_id=user_id)

        project_details_dto = self._get_project_details_dto(project_obj,
                                                       user_dto,
                                                       workflow_type_dto,
                                                       user_id)

        return project_details_dto

    def _get_workflow_type_dto(self, workflow_type_obj):

        workflow_type_dto = WorkflowTypeDto(
            name=workflow_type_obj.name,
            workflow_type_id=workflow_type_obj.id
        )

        return workflow_type_dto

    def _get_user_dto(self, user_obj):

        user_dto = UserDto(
            name=user_obj.name,
            user_id=user_obj.id,
            profile_pic= user_obj.profile_pic,
            is_admin= user_obj.is_admin
        )
        # print("\n"*10,user_dto)
        return user_dto


    def _get_project_details_dto(self,
                                 project_obj,
                                 user_dto,
                                 workflow_type_dto,
                                 user_id):

        project_details_dto = ProjectDto(
            name=project_obj.name,
            description=project_obj.description,
            workflow_type=workflow_type_dto,
            project_type=project_obj.project_type,
            created_by=self._get_user_dto(project_obj.created_by),
            created_at=project_obj.created_at,
            user_id=user_id,
            project_id=project_obj.id
        )
        return project_details_dto

    def valid_workflow_type(self, workflow_type: id)-> bool:
        is_workflow_type_id_valid = WorkflowType.objects.filter(id=workflow_type).exists()
        return is_workflow_type_id_valid

    def user_is_not_admin(self, user_id: int)-> bool:
        user_is_admin_or_not = Project.objects.filter(created_by=user_id).exists()
        return user_is_admin_or_not
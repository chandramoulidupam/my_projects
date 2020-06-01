from project_management_portal.interactors.storages.create_task_storage_interface import \
    TaskStorageInterface
from oauth2_provider.models import AccessToken
from project_management_portal.models import User, Project, Task
from project_management_portal.interactors.storages.dtos import \
    WorkflowTypeDto, UserDto, TaskDto


class CreateTaskImplementation(TaskStorageInterface):
    def create_task(self, title: str, assigned_to_id: int, project_id: int,
                               description: str, state_id: int, issue_type: str) -> int:

        user_obj = User.objects.get(id=assigned_to_id)
        # print("000000000000000000000000000",user_obj)
        user_dto = self._get_user_dto(user_obj)

        task_obj = Task.objects.create(title=title,
                                        description=description,
                                        issue_type=issue_type,
                                        state_id=state_id,
                                        project_id=project_id,
                                        assigned_to_id=assigned_to_id
                                        )
        # assigned_to = User.objects.filter(id__in=assigned_to_id)
        # project = Project.objects.get(id=project_id[0])
        # task_obj.project.add(project)
        # task_obj.assigned_to.set(assigned_to)
        task_details_dto = self._get_task_details_dto(task_obj,
                                                       user_dto)

        return task_details_dto

    def _get_user_dto(self, user_obj):

        user_dto = UserDto(
            name=user_obj.name,
            user_id=user_obj.id,
            profile_pic=user_obj.profile_pic,
            is_admin=user_obj.is_admin
        )

        return user_dto


    def _get_task_details_dto(self,
                                 task_obj,
                                 user_dto,
                                 ):
        
        task_details_dto = TaskDto(
            task_id=task_obj.id,
            title=task_obj.title,
            description=task_obj.description,
            issue_type=task_obj.issue_type,
            project_id=task_obj.project_id,
            state_id=1,
            assigned_to=user_dto
        )
        return task_details_dto

    def is_assigned_to_id_valid(self, assigned_to)-> bool:
        is_assigned_to_id_valid = User.objects.filter(id=assigned_to).exists()
        return is_assigned_to_id_valid

    def is_project_id_valid(self, project_id: int) -> bool:
        is_valid = Project.objects.filter(id=project_id).exists()
        return is_valid
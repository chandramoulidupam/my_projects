from project_management_portal.interactors.storages.get_list_of_tasks_storage_interface import \
    GetListOfTaskInterface
from oauth2_provider.models import AccessToken
# from project_management_portal.interactors.storages.dtos import \
#     UserDto, CommentDto, CommentRepliesDto
from project_management_portal.models import User, Task, WorkflowType, Project
from project_management_portal.interactors.storages.dtos import \
    WorkflowTypeDto, UserDto, ProjectDto, TaskDto


class GetListOfTaskImplementation(GetListOfTaskInterface):


    def get_list_of_tasks_for_user(self, project_id: int):

        tasks_objs = Task.objects.filter(project_id=project_id)
        # print("\n"*10,tasks_objs)
        list_of_tasks = []
        for tasks_obj in tasks_objs:
            # list_of_user_objs = tasks_obj.assigned_to
            user_dtos = self.for_user_dto(tasks_obj.assigned_to_id)
            task_dto = self._get_task_details_dto(tasks_obj,user_dtos)
            list_of_tasks.append(task_dto)
            # print("\n"*5,list_of_tasks)
        # list_of_projects = [self._get_project_details_dto(project_obj) for project_obj in project_objs]

        return list_of_tasks


    def for_user_dto(self,user_id):
        user_obj = User.objects.get(id=user_id)
        user_dto = self._get_user_dto(user_obj)
        return {
            "user_id":user_dto.user_id,
            "name": user_obj.name,
            "profile_pic": user_obj.profile_pic,
            "is_admin": user_obj.is_admin
        }


    def _get_task_details_dto(self,
                                 task_obj,
                                 user_dto,
                                 ):
        # print("\n"*10,task_obj)
        task_details_dto = TaskDto(
            title=task_obj.title,
            description=task_obj.description,
            assigned_to=user_dto,
            issue_type=task_obj.issue_type,
            project_id=task_obj.project.id,
            task_id=task_obj.id,
            state_id=task_obj.state_id
        )
        return task_details_dto

    def _get_user_dto(self, user_obj):

        user_dto = UserDto(
            name=user_obj.name,
            user_id=user_obj.id,
            profile_pic=user_obj.profile_pic,
            is_admin=user_obj.is_admin
        )

        return user_dto

    def is_user_valid(self, user_id):
        is_user_exists = User.objects.get(user_id=user_id).exists()
        return is_user_exists


    def is_assigned_to_id_valid(self, user_id):
        is_assigned_to_id_valid = Task.objects.filter(assigned_to_id=user_id).exists()
        return is_assigned_to_id_valid

    def is_project_id_valid(self, project_id):
        is_project_id_valid = Project.objects.filter(id=project_id).exists()
        return is_project_id_valid

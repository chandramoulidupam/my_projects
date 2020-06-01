from abc import ABC, abstractmethod
# from project_management_portal.interactors.storages.dtos import 


class ProjectStorageInterface(ABC):

    @abstractmethod
    def create_project(self, name: str, user_id: int, workflow_type: id, project_type: str,
                       description: str) -> int:
        pass

    @abstractmethod
    def valid_workflow_type(self, workflow_type: id)-> bool:
        pass

    @abstractmethod
    def user_is_not_admin(self, user_id)-> bool:
        pass
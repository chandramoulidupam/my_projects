from abc import ABC, abstractmethod
# from project_management_portal.interactors.storages.dtos import 


class TaskStorageInterface(ABC):

    @abstractmethod
    def create_task(self, title: str, assigned_to_id: int,
                               description: str, state_id: int, issue_type: str, project_id: int) -> int:
        pass

    @abstractmethod
    def is_assigned_to_id_valid(self, assigned_to: int)-> bool:
        pass

    @abstractmethod
    def is_project_id_valid(self, project_id: int) -> bool:
        pass
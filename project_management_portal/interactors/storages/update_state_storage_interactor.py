from abc import ABC, abstractmethod
# from project_management_portal.interactors.storages.dtos import 


class StateUpdateStorageInterface(ABC):

    @abstractmethod
    def state_update(self, to_state_id: int,name: str, project_id: int, task_id: int):
        pass

    @abstractmethod
    def valid_project_id(self, project_id: id)-> bool:
        pass

    @abstractmethod
    def valid_task_id(self, task_id)-> bool:
        pass

    @abstractmethod
    def valid_to_state_id(self, to_state_id)-> bool:
        pass
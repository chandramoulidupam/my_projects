from abc import ABC, abstractmethod
# from project_management_portal.interactors.storages.dtos import 

class GetListOfTaskInterface(ABC):

    @abstractmethod
    def get_list_of_tasks_for_user(self, project_id: int):
        pass

    @abstractmethod
    def is_project_id_valid(self, project_id: int):
        pass

    @abstractmethod
    def is_assigned_to_id_valid(self, user_id: int):
        pass
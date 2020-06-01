from abc import ABC, abstractmethod
# from project_management_portal.interactors.storages.dtos import 

class GetListOfProjectInterface(ABC):

    @abstractmethod
    def get_list_of_project_for_user(self, user_id: str):
        pass

    @abstractmethod
    def get_list_of_project_for_admin(self, user_id: str, offset: int, limit: int):
        pass

    @abstractmethod
    def is_user_admin(self, user_id: str):
        pass

    @abstractmethod
    def is_user_valid(self, user_id: str):
        pass
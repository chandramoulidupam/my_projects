from abc import ABC, abstractmethod
# from project_management_portal.interactors.storages.dtos import 

class UserLoginStorageInterface(ABC):

    @abstractmethod
    def user_login(self, username: str, password: str):
        pass

    @abstractmethod
    def valid_username(self, username: str) -> bool:
        pass

    @abstractmethod
    def valid_password(self, username: str, password: str) ->bool:
        pass

from abc import ABC, abstractmethod
# from project_management_portal.interactors.storages.dtos import 


class UserLogoutStorageInterface(ABC):

    @abstractmethod
    def user_logout(self):
        pass

    @abstractmethod
    def valid_accesstoken(self, access_token: str) ->bool:
        pass

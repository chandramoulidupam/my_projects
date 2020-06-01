from project_management_portal.interactors.presenters.presenter_interface import \
    PresenterInterface
from project_management_portal.interactors.storages.user_logout_storage_interface import \
    UserLogoutStorageInterface
class LogoutInteractor:
    def __init__(self, storage: UserLogoutStorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter
    
    def user_logout(self, access_token: str):
        is_access_token_valid = self.storage.valid_accesstoken(access_token)
        if not is_access_token_valid:
            self.presenter.raise_exception_for_invalid_access_token()
            return
        else:
            self.presenter.delete_accesstoken(token=access_token)
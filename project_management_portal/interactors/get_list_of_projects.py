from project_management_portal.interactors.presenters.presenter_interface import \
    PresenterInterface
from project_management_portal.interactors.storages.get_list_of_projects_storage_interface import \
    GetListOfProjectInterface
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import * 

class GetListOfProjectInteractor:
    def __init__(self, storage: GetListOfProjectInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter
    
    def get_list_of_project(self, user_id: id, offset: int, limit: int):

        is_user_valid = self.storage.is_user_valid(user_id)
        if not is_user_valid:
            self.presenter.raise_exception_for_invalid_user_id(user_id)
            return
        is_user_admin = self.storage.is_user_admin(user_id)
        if not is_user_admin:
            projects = self.storage.get_list_of_project_for_user(
                user_id=user_id,
                offset=offset,
                limit=limit
            )
        else:
            projects = self.storage.get_list_of_project_for_admin(
                user_id=user_id,
                offset=offset,
                limit=limit
            )
        # print("\n"*10,projects,"\n"*10)
        return self.presenter.get_list_of_project_response(
            projects
        )

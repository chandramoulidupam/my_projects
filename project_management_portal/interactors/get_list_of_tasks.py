from project_management_portal.interactors.presenters.presenter_interface import \
    PresenterInterface
from project_management_portal.interactors.storages.get_list_of_tasks_storage_interface import \
    GetListOfTaskInterface
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import * 

class GetListOfTaskInteractor:
    def __init__(self, storage: GetListOfTaskInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter
    
    def get_list_of_tasks_for_user(self, project_id: int):
        is_project_id_valid = self.storage.is_project_id_valid(project_id)
        if not is_project_id_valid:
            self.presenter.raise_exception_for_invalid_project_id(project_id)
            return
        # is_user_valid = self.storage.is_user_valid(user_id)
        # print("************************************"*10, user_id)
        tasks = self.storage.get_list_of_tasks_for_user(
                project_id=project_id
        )
        # print(tasks,"\n","storage")
        return self.presenter.get_list_of_task_response(
            tasks
        )

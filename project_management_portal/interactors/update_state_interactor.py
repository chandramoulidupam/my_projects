from project_management_portal.interactors.presenters.presenter_interface import \
    PresenterInterface
from project_management_portal.interactors.storages.update_state_storage_interactor import \
    StateUpdateStorageInterface
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import * 

class StateUpdateInteractor:
    def __init__(self, storage: StateUpdateStorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter
    
    def state_update(self, to_state_id: int,name: str, project_id: int, task_id: int):

        is_to_state_id_valid = self.storage.valid_to_state_id(to_state_id=to_state_id)
        if not is_to_state_id_valid:
            self.presenter.raise_exception_for_invalid_to_state_id(to_state_id)
            return
        is_project_id_valid = self.storage.valid_project_id(project_id=project_id)
        if not is_project_id_valid:
            self.presenter.raise_exception_for_invalid_project_id(project_id)
            return
        is_task_id_valid = self.storage.valid_task_id(task_id=task_id)
        if not is_task_id_valid:
            self.presenter.raise_exception_for_invalid_task_id(task_id)
            return

        self.storage.state_update(
            to_state_id=to_state_id,
            name=name,
            project_id=project_id,
            task_id=task_id
        )

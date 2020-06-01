from project_management_portal.interactors.presenters.presenter_interface import \
    PresenterInterface
from project_management_portal.interactors.storages.create_task_storage_interface import \
    TaskStorageInterface
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import * 

class CreateTaskInteractor:
    def __init__(self, storage: TaskStorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter
    
    def create_task(self, title: str, description: str, issue_type: str, assigned_to_id: int, state_id: int, project_id: int):
        valid_assigned_to = self.storage.is_assigned_to_id_valid(assigned_to=assigned_to_id)
        if not valid_assigned_to:
            self.presenter.raise_exception_for_invalid_assigned_id(assigned_to_id)
            return
        valid_project_id = self.storage.is_project_id_valid(project_id=project_id)
        if not valid_project_id:
            self.presenter.raise_exception_for_invalid_project_id(project_id)
            return
        # user_id = self.storage.is_user_admin
        new_task_obj = self.storage.create_task(
            title=title,
            description=description,
            issue_type=issue_type,
            assigned_to_id=assigned_to_id,
            state_id=state_id,
            project_id=project_id
        )

        return self.presenter.get_create_task_response(new_task_obj)

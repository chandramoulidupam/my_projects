from project_management_portal.interactors.presenters.presenter_interface import \
    PresenterInterface
from project_management_portal.interactors.storages.create_project_storage_interface import \
    ProjectStorageInterface
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import * 

class CreateProjectInteractor:
    def __init__(self, storage: ProjectStorageInterface,
                 presenter: PresenterInterface):
        self.storage = storage
        self.presenter = presenter
    
    def create_project(self, name: str, description: str, workflow_type: id, project_type: str, user_id: int):

        valid_workflow_type_id = self.storage.valid_workflow_type(workflow_type=workflow_type)
        if not valid_workflow_type_id:
            self.presenter.raise_exception_for_invalid_workflow_type()
            return
        user_is_admin = self.storage.user_is_not_admin(user_id=user_id)
        if not user_is_admin:
            self.presenter.raise_exception_for_user_is_not_admin(user_id)
            return
        # user_id = self.storage.is_user_admin
        new_project_id = self.storage.create_project(
            name=name,
            description=description,
            workflow_type=workflow_type,
            project_type=project_type,
            user_id=user_id
        )

        return self.presenter.get_create_project_response(
            new_project_id
        )

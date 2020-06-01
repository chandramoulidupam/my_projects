from project_management_portal.interactors.storages.update_state_storage_interactor import \
    StateUpdateStorageInterface
from oauth2_provider.models import AccessToken
from project_management_portal.models import User, Project, Task
from project_management_portal.interactors.storages.dtos import \
    WorkflowTypeDto, UserDto, TaskDto


class StateUpdateImplementation(StateUpdateStorageInterface):
    def state_update(self, taskid: int, project_id: int,
                               name: str, to_state_id: int) -> int:
        pass

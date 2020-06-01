from project_management_portal.interactors.presenters.presenter_interface import \
    PresenterInterface
from project_management_portal.interactors.storages.user_login_storage_interface import \
    UserLoginStorageInterface
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import * 
from django.contrib.auth import authenticate


class LoginInteractor:
    def __init__(self, storage: UserLoginStorageInterface,
                 oauth_storage: OAuth2SQLStorage,
                 presenter: PresenterInterface):
        self.storage = storage
        self.oauth_storage = oauth_storage
        self.presenter = presenter
    
    def user_login(self, username: str, password: str):

        valid_username = self.storage.valid_username(username=username)

        if not valid_username:
            self.presenter.raise_exception_for_invalid_username()
            return

        valid_password = self.storage.valid_password(username=username,password=password)

        if not valid_password:
            self.presenter.raise_exception_for_invalid_password()
            return
        user = authenticate(username=username,password=password)
        
        user_id = user.id
        storage = OAuth2SQLStorage()
        service = OAuthUserAuthTokensService(oauth2_storage=storage)    
        token_dto = service.create_user_auth_tokens(user_id=user_id)
        print(token_dto)
        self.presenter.get_acces_token_dto_response(token=token_dto)

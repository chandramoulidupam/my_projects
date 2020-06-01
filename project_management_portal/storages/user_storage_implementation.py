from project_management_portal.interactors.storages.user_login_storage_interface import \
    UserLoginStorageInterface
from project_management_portal.interactors.storages.user_logout_storage_interface import \
    UserLogoutStorageInterface
from project_management_portal.interactors.storages.get_list_of_projects_storage_interface import \
    GetListOfProjectInterface
from oauth2_provider.models import AccessToken
# from project_management_portal.interactors.storages.dtos import \
#     UserDto, CommentDto, CommentRepliesDto
from project_management_portal.models import User
from project_management_portal.exceptions.exceptions import InvalidPassword, InvalidUsername

class LoginStorageImplementation(UserLoginStorageInterface):

    def valid_username(self, username: str):
        is_valid_username= User.objects.filter(name=username).exists()
        return is_valid_username

    def valid_password(self, username: str, password: str):
        user= User.objects.get(name=username)
        return user.check_password(password)
    
    def user_login(self, username: str, password: str):
        pass

class LogoutStorageImplementation(UserLogoutStorageInterface):
    def valid_accesstoken(self, access_token: str):
        try:
            AccessToken.objects.get(token=access_token)
        except AccessToken.DoesNotExist:
            token=None
        if token is not None:
            return True
    def delete_accesstoken(self,access_token:str):
        token = AccessToken.objects.get(token=access_token)
        token.delete()

    def user_logout(self):
        pass


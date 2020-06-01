# import pytest
# from django_swagger_utils.drf_server.exceptions import NotFound
# from unittest.mock import create_autospec
# from project_management_portal.storages.user_storage_implementation import \
#     LogoutStorageImplementation


# @pytest.mock.django_db
# class TestUserLogoutStorager:
#     def test_access_token(self, users):

#         # Arrange
#         user1 = users[0]
#         user1 = user1.username
#         storage = LogoutStorageImplementation()
#         # Act
#         storage.valid_accesstoken(username=user1)

#         # Assert
        

#     def test_delete_access_token(self, users):
#         # Arrange
#         access_token = "123456"
#         storage = LogoutStorageImplementation()
#         # Act
#         storage.delete_accesstoken(access_token=access_token)
#         # Assert

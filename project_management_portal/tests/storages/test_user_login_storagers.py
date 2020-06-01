# import pytest
# from django_swagger_utils.drf_server.exceptions import NotFound
# from unittest.mock import create_autospec
# from project_management_portal.storages.user_storage_implementation import \
#     LoginStorageImplementation


# @pytest.mock.django_db
# class TestUserLoginStorager:
#     def test_username_is_valid(self, users):

#         # Arrange
#         user1 = users[0]
#         user1 = user1.username
#         storage = LoginStorageImplementation()
#         # Act
#         storage.valid_username(username=user1)

#         # Assert
        

#     def test_password_is_valid(self, users):
#         # Arrange
#         user1 = users[0]
#         username1 = user1.username
#         password1 = user1.password
#         storage = LoginStorageImplementation()
#         # Act
#         storage.valid_password(username=username1, password=password1)
#         # Assert
        
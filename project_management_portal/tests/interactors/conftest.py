import pytest
from project_management_portal.models import User

@pytest.fixture()
def users():
    list_of_users = [
        User(username="user1",password="user1passowrd"),
        User(username="user2",password="user2passowrd"),
        User(username="user3",password="user3passowrd")
        ]
    User.objects.bulk_create(list_of_users)
    users = User.objects.all()
    return users


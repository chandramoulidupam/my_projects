# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "logout"
REQUEST_METHOD = "post"
URL_SUFFIX = "user/logout/v1/"

from .test_case_01 import TestCase01LogoutAPITestCase

__all__ = [
    "TestCase01LogoutAPITestCase"
]

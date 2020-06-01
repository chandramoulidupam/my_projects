# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "login"
REQUEST_METHOD = "post"
URL_SUFFIX = "user/login/v1/"

from .test_case_01 import TestCase01LoginAPITestCase

__all__ = [
    "TestCase01LoginAPITestCase"
]

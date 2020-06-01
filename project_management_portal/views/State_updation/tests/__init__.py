# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "State_updation"
REQUEST_METHOD = "post"
URL_SUFFIX = "projects/{project_id}/tasks/{task_id}/transition/v1/"

from .test_case_01 import TestCase01StateUpdationAPITestCase

__all__ = [
    "TestCase01StateUpdationAPITestCase"
]

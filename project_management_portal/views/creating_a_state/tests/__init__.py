# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "creating_a_state"
REQUEST_METHOD = "post"
URL_SUFFIX = "projects/state/v1/"

from .test_case_01 import TestCase01CreatingAStateAPITestCase

__all__ = [
    "TestCase01CreatingAStateAPITestCase"
]

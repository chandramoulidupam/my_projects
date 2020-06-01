# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "creating_a_transition"
REQUEST_METHOD = "post"
URL_SUFFIX = "projects/transition/v1/"

from .test_case_01 import TestCase01CreatingATransitionAPITestCase

__all__ = [
    "TestCase01CreatingATransitionAPITestCase"
]

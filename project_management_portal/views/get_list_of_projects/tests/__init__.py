# pylint: disable=wrong-import-position

APP_NAME = "project_management_portal"
OPERATION_NAME = "get_list_of_projects"
REQUEST_METHOD = "get"
URL_SUFFIX = "projects/list_of_projects/v1/"

from .test_case_01 import TestCase01GetListOfProjectsAPITestCase

__all__ = [
    "TestCase01GetListOfProjectsAPITestCase"
]

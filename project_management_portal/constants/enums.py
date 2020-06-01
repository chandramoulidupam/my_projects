from enum import Enum

from ib_common.constants import BaseEnumClass


class ProjectType(BaseEnumClass, Enum):
     CLASSICSOFTWARE = 'CLASSICSOFTWARE'
     FINANCIAL = 'FINANCIAL'
     CRM = 'CRM'


class IssueType(BaseEnumClass, Enum):
     Task ="Task"
     Bug = "Bug"
     Developerstory ="Developer_Story"
     Userstory = "User_Story"
     Enhancement = "Enhancement"
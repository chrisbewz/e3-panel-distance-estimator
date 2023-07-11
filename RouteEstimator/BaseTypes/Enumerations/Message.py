from enum import Enum

class MSG_KIND(Enum):
    ERROR = 0,
    WARNING = 1,
    COMMOM = 2

class MSG_AWAIT(Enum):
    IGNORE = 0
    POP = 1
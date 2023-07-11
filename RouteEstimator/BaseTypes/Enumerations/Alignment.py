from enum import Enum


class ALIGN_DIRECTIONS(Enum):
    LEFT = 1
    RIGHT = 2
    CENTER_HORIZONTALLY = 3
    CENTER_VERTICALLY = 4
    TOP = 5
    BOTTOM = 6


class ALIGNMENT_RESULT(Enum):
    SUCESS = 0
    NO_PROJECT = -1
    NO_SHEET_DEFINED = -2
    INVALID_REF_ITEM = -3
    SOME_ID_INVALID = -4
    INVALID_MODE = 5


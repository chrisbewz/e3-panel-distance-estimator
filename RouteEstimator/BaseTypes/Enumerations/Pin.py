from enum import Enum


class P_FUNC(Enum):
    '''Functions related to the current utility of a device pin'''
    UNDEF = 0,
    POWER_GROUND = 1,
    NO_CONNECTION = 2,
    INPUT = 3,
    OUTPUT = 4,
    IN_AND_OUT = 5,
    OPEN_COLLECTOR = 6


class PIN_ATT_VALUES(Enum):
    '''Pin indication to add an desired attribute based on pin core position'''
    START = 1,
    END = 2


class PIN_TYPES(Enum):
    UNDEF = 0
    DEVICE = 1
    CONNECTOR = 2
    BLOCK_CONNECTOR = 3
    COMPONENT = 4
    NORMAL_MODE = 5
    CONNECTOR_SYMBOL = 6
    NET_NODE = 7
    WIRE_COUNT = 8
    TEMPLATE_SYMBOL = 9
    SHEET_REF = 10
    SIGNAL_CARRY_NODE = 11
    CABWIR = 12
    HOSE = 13
    TUBE = 14
    CONDUCTOR_WIRE_CHANGE = 15
    HOSE_CHANGE = 16
    TUBE_CHANGE = 17

class PIN_PLACEMENT(Enum):
    UNPLACED = 0
    PLACED = 1

class PIN_SIDE(Enum):
    COMMOM_END = 1
    WIRE_END = 2

class PIN_DIRECTIONS(Enum):
    ALL = 0
    RIGTH = 1
    TOP = 3
    LEFT = 5
    BOTTOM = 7
    VERTICAL = 9
    HORIZONTAL = 10
    AUTO = 14

class PIN_CONNECTION_KIND(Enum):
    UNKNOWN = 0
    SCREWED = 1
    CLAMPED = 2
    SOLDED = 3

class PIN_CAVITY_KIND(Enum):
    ALL = 0
    PINT_TERMINAL = 1
    WIRE_SEAL = 2
    PLUG = 3

class PIN_END_KIND(Enum):
    FIRST_CORE = 1
    LAST_CORE = 2

class PIN_NODE_KIND(Enum):
    OPEN = 0
    CONNECTOR_MODE = 1
    NORMAL_SYMBOL = 2
    NET_NODE = 3
    MULTIPLE_LINES_OPT1 = 4
    MULTIPLE_LINES_OPT2 = 7
    SPECIAL_NODE = 5
    HIERARCHICAL_PORT_NODE = 8
    WIRE_COUNT_NODE = 11

from ...BaseTypes.Contracts.SchemaBase import SchemaBase
from ...BaseTypes.Enumerations.Pin import PIN_PLACEMENT


class PinSchema(SchemaBase):

    __row = None
    __placement: PIN_PLACEMENT = None

    def __init__(self, placeState: PIN_PLACEMENT, xLoc: any, yLoc: any, grid: str, col: any, val: any):
        super().__init__(xLoc, yLoc, grid, col)
        self.__placement: PIN_PLACEMENT = placeState
        self.__row = val


    @property
    def placement(self):
        return self.__placement

    @property
    def row(self):
        return self.__row


class SymbolSchema(SchemaBase):

    __row = None

    def __init__(self, xLoc: any, yLoc: any, grid: str, col: any, row: any):
        super().__init__(xLoc, yLoc, grid, col)
        self.__row = row

    @property
    def row(self):
        return self.__row
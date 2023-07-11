class SchemaBase:
    __xLocation = None
    __yLocation = None
    __grid = None
    __column = None

    def __init__(self, xLoc: any, yLoc: any, grid: str, col: any):
        self.__xLocation = xLoc
        self.__yLocation = yLoc
        self.__grid = grid
        self.__column = col

    @property
    def yLocation(self):
        return self.__yLocation

    @property
    def xLocation(self):
        return self.__xLocation

    @property
    def column(self):
        return self.__column

    @property
    def grid(self):
        return self.__grid

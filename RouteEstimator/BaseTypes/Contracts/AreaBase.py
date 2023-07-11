

class AreaBase:

    __x_min: float = None
    __y_min: float = None
    __x_max: float = None
    __y_max: float = None

    def __init__(self, xma: float, xmi: float, yma: float, ymi: float):
        self.__x_min = xmi
        self.__x_max = xma
        self.__y_min = ymi
        self.__y_max = yma

    @property
    def maxY(self):
        return self.__y_max

    @property
    def maxX(self):
        return self.__x_max

    @property
    def minY(self):
        return self.__y_min

    @property
    def minX(self):
        return self.__x_min

    @classmethod
    def Initialize(cls):
        return cls(0, 0, 0, 0)
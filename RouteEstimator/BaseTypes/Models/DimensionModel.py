

class Dimension:
    __x: float = None
    __y: float = None
    __z: float = None

    def __init__(self, x: float, y: float, z: float):
        self.__z = z
        self.__x = x
        self.__y = y

    @property
    def xValue(self):
        return self.__x

    @property
    def yValue(self):
        return self.__y

    @property
    def zValue(self):
        return self.__z

    def  __str__(self):
        return f"X: [{self.__x}] Y: [{self.__y}] Z:[{self.__z}]"

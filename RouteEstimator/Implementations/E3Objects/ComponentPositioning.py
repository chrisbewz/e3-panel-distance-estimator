from ...BaseTypes.Interfaces.IPointAbstract import IPointAbstract
from ...BaseTypes.Models.CartesianModel import CartesianPoint


class PinPosition:
    __coordinates: IPointAbstract = None

    def __init__(self, x, y, z):
        self.__coordinates = CartesianPoint(x, y, z)

    @property
    def coordinates(self):
        return self.__coordinates

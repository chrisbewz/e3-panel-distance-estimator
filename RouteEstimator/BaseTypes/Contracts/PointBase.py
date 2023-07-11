from abc import ABC, abstractmethod, abstractclassmethod, ABCMeta
from multipledispatch import dispatch
from ...BaseTypes.Interfaces.IPointAbstract import IPointAbstract
from ...Extensions.Point import PointConverters
from math import (

    cos, sin, atan, sqrt, dist
)


class PointBase(ABC):

    @abstractclassmethod
    def CreateInitial(cls):
        pass

    @abstractmethod
    def Reset(self):
        pass

    @abstractmethod
    def EuclideanDistance(self, p2):
        pass


class PolarBase(IPointAbstract):
    _mag = None
    _theta = None

    def __init__(self, mag, phase):
        super().__init__()
        self._mag = mag
        self._theta = phase

    @property
    def magnitude(self):
        return self._mag

    @property
    def phase(self):
        return self._theta

    @classmethod
    def CreateInitial(cls):
        return cls(0, 0)

    def Reset(self):
        self._mag = None
        self._theta = None

    def EuclideanDistance(self, p2):
        return sqrt(pow(self.magnitude, 2) + pow(p2.magnitude, 2) - (
                (2 * self.magnitude * p2.magnitude) * cos(p2.phase - self.phase)))

    @classmethod
    def Create(cls, mag, phase):
        return cls(mag, phase)

    @classmethod
    @dispatch(ABCMeta, float, float)
    def FromCartesian(cls, x, y):
        return cls.__convertFromCartesian(x, y)

    def ToCartesian(self):
        return PointConverters.AsCartesian(self.magnitude, self.phase)

    def AsArray(self):
        return [self.magnitude, self.phase]

    @classmethod
    def __convertToCartesian(cls, mag, phase):
        return (mag * cos(phase)), (mag * sin(phase))

    @classmethod
    def __convertFromCartesian(cls, xCoord, yCoord):
        if xCoord == 0:
            raise ZeroDivisionError("O valor de x não pode ser nulo para conversão para forma polar")
        return cls.Create(sqrt(pow(xCoord, 2) + pow(yCoord, 2)), (atan(yCoord / xCoord)))

    def __eq__(self, other):
        if isinstance(other, CartesianBase):
            _cart = self.FromCartesian(other.xPos, other.yPos)
            return self.__eq__(_cart)

        elif isinstance(other, PolarBase):
            return (self.magnitude == other.magnitude) and (self.phase == other.phase)

        else:
            raise ValueError("O tipo informado não é válido para conversão")

    def __ge__(self, other):
        if isinstance(other, CartesianBase):
            _cart = self.FromCartesian(other.xPos, other.yPos)
            return self.__eq__(other) or _cart.magnitude > self.magnitude and _cart.magnitude > self.magnitude
        elif isinstance(other, PolarBase):
            return self.__eq__(other) or self.magnitude > other.magnitude and self.phase > other.phase
        else:
            raise ValueError("O tipo informado não é válido para conversão")

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __lt__(self, other):
        if isinstance(other, CartesianBase):
            _cart = self.FromCartesian(other.xPos, other.yPos)
            return self.phase < _cart.phase and self.magnitude < _cart.magnitude

        elif isinstance(other, PolarBase):
            return self.magnitude < other.magnitude and self.phase < other.phase

        else:
            raise ValueError("O tipo informado não é válido para conversão")

    def __gt__(self, other):
        if isinstance(other, CartesianBase):
            _cart = self.FromCartesian(other.xPos, other.yPos)

            return self.phase > _cart.phase and self.magnitude > _cart.magnitude
        elif isinstance(other, PolarBase):
            return self.magnitude > other.magnitude and self.phase > other.phase
        else:
            raise ValueError("O tipo informado não é válido para conversão")

    def __ne__(self, other):
        if isinstance(other, CartesianBase):
            _cart = self.FromCartesian(other.xPos, other.yPos)
            return not (self.__eq__(other))

        elif isinstance(other, PolarBase):
            return (self.magnitude != other.magnitude) and (self.phase != other.phase)

        else:
            raise ValueError("O tipo informado não é válido para conversão")

    def __mul__(self, other):
        if isinstance(other, CartesianBase):
            _newMag, _newPhase = self.FromCartesian(other.xPos, other.yPos)
            return self.Create(self.magnitude * _newMag, self.phase + _newPhase)

        elif isinstance(other, PolarBase):
            return self.Create(self.magnitude * other.magnitude, self.phase + other.phase)

        raise ValueError("O tipo do argumento é inválido para realizar a operação")

    def __sub__(self, other):
        if isinstance(other, CartesianBase):

            _p1C = self.ToCartesian()
            return self.Create(self.FromCartesian(_p1C.xPos - other.xPos, _p1C.yPos - other.yPos))

        elif isinstance(other, PolarBase):

            _p1C = other.ToCartesian()
            _p2C = self.ToCartesian()

            return _p2C.__sub__(_p1C).ToPolar()

        raise ValueError("O tipo do argumento é inválido para realizar a operação")

    def __add__(self, other):

        if isinstance(other, CartesianBase):
            _p1C = self.ToCartesian()
            return self.Create(self.FromCartesian(_p1C.xPos + other.xPos, _p1C.yPos + other.yPos))

        elif isinstance(other, PolarBase):
            _p1C = other.ToCartesian()
            _p2C = self.ToCartesian()
            return _p2C.__add__(_p1C).ToPolar()

        else:
            raise ValueError("O tipo do argumento é inválido para realizar a operação")

    def __truediv__(self, other):

        if isinstance(other, CartesianBase):
            _p2P = other.ToPolar()
            return self.Create(self.magnitude / _p2P.magnitude, self.phase - _p2P.phase)

        elif isinstance(other, PolarBase):
            return self.Create(self.magnitude / other.magnitude, self.phase - other.phase)
        else:
            raise ValueError("O tipo do argumento é inválido para realizar a operação")


class CartesianBase(IPointAbstract):
    _xPos = None
    _yPos = None
    _zPos = None

    def __init__(self, xCoord, yCoord, zCoord):
        super().__init__()
        self._xPos = xCoord
        self._yPos = yCoord
        self._zPos = zCoord

    @property
    def xPos(self):
        return self._xPos

    @property
    def yPos(self):
        return self._yPos

    @property
    def zPos(self):
        return self._zPos

    @classmethod
    def CreateInitial(cls):
        return cls(0, 0, 0)

    @classmethod
    def Create(cls, xCoord, yCoord, zCoord):
        return cls(xCoord, yCoord, zCoord)

    def Reset(self):
        self._xPos = None
        self._yPos = None
        self._zPos = None

    def ToPolar(self):
        return PointConverters.AsPolar(self)

    @classmethod
    def FromPolar(cls, mag, phase):
        return cls.Create(mag * cos(phase), mag * sin(phase), 0)

    def AsArray(self):
        return [self._xPos, self._yPos, self._zPos]

    def EuclideanDistance(self, p2):
        return dist(self.AsArray(), p2.AsArray())

    def __eq__(self, other):
        if isinstance(other, PolarBase):
            return (self.xPos == other.magnitude * cos(other.phase)) and (
                    self.yPos == other.magnitude * sin(other.phase))
        elif isinstance(other, CartesianBase):
            return (self.xPos == other.xPos) and (self.yPos == other.yPos) and (self.zPos == other.zPos)

        else:
            raise ValueError("O tipo do argumento é inválido para realizar a operação")

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __lt__(self, other):
        if isinstance(other, PolarBase):

            _x = other.magnitude * cos(other.phase)
            _y = other.magnitude * sin(other.phase)

            return self.xPos < _x and self.yPos < _y

        elif isinstance(other, CartesianBase):
            return self.xPos < other.xPos and self.yPos < other.yPos and self.zPos < other.zPos

        else:
            raise ValueError("O tipo do argumento é inválido para realizar a operação")

    def __gt__(self, other):
        if isinstance(other, PolarBase):

            _x = other.magnitude * cos(other.phase)
            _y = other.magnitude * sin(other.phase)

            return self.xPos > _x and self.yPos > _y

        elif isinstance(other, CartesianBase):
            return self.xPos > other.xPos and self.yPos > other.yPos and self.zPos > other.zPos

        else:
            raise ValueError("O tipo do argumento é inválido para realizar a operação")

    def __ne__(self, other):
        if isinstance(other, PolarBase):

            _x = other.magnitude * cos(other.phase)
            _y = other.magnitude * sin(other.phase)

            return (self.xPos != _x) and (self.yPos != _y)

        elif isinstance(other, CartesianBase):
            return (self.xPos != other.xPos) and (self.yPos != other.yPos) and (self.zPos != other.zPos)

        else:
            raise ValueError("O tipo do argumento é inválido para realizar a operação")

    def __mul__(self, other):
        if isinstance(other, PolarBase):

            _x = other.magnitude * cos(other.phase)
            _y = other.magnitude * sin(other.phase)

            return self.Create(self.xPos * _x, self.yPos * _y, self.zPos)

        elif isinstance(other, CartesianBase):
            return self.Create(self.xPos * other.xPos, self.yPos * other.yPos, self.zPos * other.zPos)

        else:
            raise ValueError("O tipo do argumento é inválido para realizar a operação")

    def __sub__(self, other):
        if isinstance(other, PolarBase):

            _x = other.magnitude * cos(other.phase)
            _y = other.magnitude * sin(other.phase)

            return self.Create(self.xPos - _x, self.yPos - _y, self.zPos)

        elif isinstance(other, CartesianBase):
            return self.Create(self.xPos - other.xPos, self.yPos - other.yPos, self.zPos - other.zPos)

        else:
            raise ValueError("O tipo do argumento é inválido para realizar a operação")

    def __add__(self, other):
        if isinstance(other, PolarBase):

            _x = other.magnitude * cos(other.phase)
            _y = other.magnitude * sin(other.phase)

            return self.Create(self.xPos + _x, self.yPos + _y, self.zPos)

        elif isinstance(other, CartesianBase):
            return self.Create(self.xPos + other.xPos, self.yPos + other.yPos, self.zPos + other.zPos)

        else:
            raise ValueError("O tipo do argumento é inválido para realizar a operação")

    def __truediv__(self, other):
        if isinstance(other, PolarBase):

            _x = other.magnitude * cos(other.phase)
            _y = other.magnitude * sin(other.phase)

            if _x is not 0 and _y is not 0:
                return self.Create(self.xPos / _x, self.yPos / _y, self.zPos)

        elif isinstance(other, CartesianBase):
            if other.xPos is not 0 and other.yPos is not 0 and other.zPos is not 0:
                return self.Create(self.xPos / other.xPos, self.yPos / other.yPos, self.zPos / other.zPos)
            else:
                raise ValueError("As coordenadas do ponto 2 devem ser diferentes de zero")
        else:
            raise ValueError("O tipo do argumento é inválido para realizar a operação")

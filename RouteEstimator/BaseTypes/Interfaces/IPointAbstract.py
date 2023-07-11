from abc import (
    ABC, ABCMeta,
    abstractmethod, abstractclassmethod,

)


class IPointAbstract(ABC):

    def __init__(self) -> None:
        pass

    @abstractclassmethod
    def CreateInitial(cls):
        pass

    @abstractmethod
    def Reset(self):
        pass

    @abstractmethod
    def EuclideanDistance(self, p2):
        pass

    @abstractmethod
    def AsArray(self):
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __div__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __le__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __lt__(self, other):
        pass

    def __ne__(self, other):
        pass

from abc import ABC, abstractmethod,abstractstaticmethod,abstractclassmethod
from multipledispatch import dispatch


class AbstractMapper(ABC):
    @dispatch((int, tuple))
    @abstractmethod
    def Map(self, arg: (int, tuple)):
        """Maps e3 pin destination information from a tuple of id's to a dict of values"""
        pass

    @dispatch(list)
    @abstractmethod
    def Map(self, *args: list):
        """Maps e3 pin destination information from a tuple of id's to a dict of values"""
        pass

    @dispatch(object, int)
    @abstractmethod
    def Map(object, identifier: int):
        pass

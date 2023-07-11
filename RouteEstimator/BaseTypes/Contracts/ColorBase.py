from abc import ABC, abstractmethod, abstractproperty, abstractclassmethod

class ColorBase(ABC):

    @abstractmethod
    def Value(self):
        return self

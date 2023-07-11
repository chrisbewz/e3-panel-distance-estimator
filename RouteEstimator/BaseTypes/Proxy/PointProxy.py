from ...BaseTypes.Interfaces.IPointAbstract import IPointAbstract


class Point(IPointAbstract):

    def AsArray(self):
        pass

    def __init__(self, pointKind):
        self.__class__ = pointKind[0]
        self.__class__.CreateInitial()


    @classmethod
    def CreateInitial(cls):
        pass

    def Reset(self):
        pass

    def EuclideanDistance(self, p2):
        pass
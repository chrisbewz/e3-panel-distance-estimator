from ...BaseTypes.Contracts.PointBase import PolarBase


class PolarPoint(PolarBase):

    def __init__(self, mag=None, phase=None):
        super().__init__(mag, phase)



from RouteEstimator.BaseTypes.Contracts.AreaBase import AreaBase


class DrawingArea(AreaBase):

    def __init__(self, xma: float, xmi: float, yma: float, ymi: float):
        super().__init__(xma, xmi, yma, ymi)

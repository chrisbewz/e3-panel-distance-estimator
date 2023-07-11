from RouteEstimator.BaseTypes.Handlers.GraphBase import GraphBase
from RouteEstimator.BaseTypes.Models.CartesianModel import CartesianPoint


class GraphComponent(GraphBase):

    def __init__(self, identifier: int):
        super().__init__(identifier)

    def Arc(self, sheetIdentifier: int, posX: float, posY: float, startAngle, endAngle) -> int:
        return self.instance.CreateArc(sheetIdentifier, posX, posY, startAngle, endAngle)

    def Circle(self, sheetIdentifier: int, posX: float, posY: float, startAngle, endAngle) -> int:
        return self.instance.CreateCircle(sheetIdentifier, posX, posY, startAngle, endAngle)

    def Cloud(self, sheetIdentifier: int, points: list[CartesianPoint]) -> int:
        xArr: list[float] = [p.xPos for p in points]
        yArr: list[float] = [p.yPos for p in points]
        return self.instance.CreateCloud(sheetIdentifier, len(points), xArr, yArr)

    def Curve(self, sheetIdentifier: int, points: list[CartesianPoint]) -> int:
        xArr: list[float] = [p.xPos for p in points]
        yArr: list[float] = [p.yPos for p in points]
        return self.instance.CreateCurve(sheetIdentifier, len(points), xArr, yArr)

    def Measure(self, sheetIdentifier: int, startX, startY, endX, endY) -> int:
        return self.instance.CreateCurve(sheetIdentifier, startX, startY, endX, endY)

    def Polygon(self, sheetIdentifier: int, points: list[CartesianPoint]) -> int:
        xArr: list[float] = [p.xPos for p in points]
        yArr: list[float] = [p.yPos for p in points]

        return self.instance.CreatePolygon(sheetIdentifier, len(points), xArr, yArr)

    def Rectangle(self, sheetIdentifier: int, startX: float, startY: float, endX: float, endY: float) -> int:
        return self.instance.CreateRectangle(sheetIdentifier, startX, startY, endX, endY)

    def RotatedText(self, sheetIdentifier: int, content: str, posX: float, posY: float, rotation: float) -> int:
        return self.instance.CreateRectangle(sheetIdentifier, content, posX, posY, rotation)

















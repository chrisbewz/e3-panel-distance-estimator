class PointConverters:

    @classmethod
    def AsPolar(cls, point):
        from ..BaseTypes.Models.PolarModel import PolarPoint
        return PolarPoint.FromCartesian(float(point.xPos), float(point.yPos))

    @classmethod
    def AsCartesian(cls, mag,phase):
        from ..BaseTypes.Models.CartesianModel import CartesianPoint
        return CartesianPoint.FromPolar(mag, phase)

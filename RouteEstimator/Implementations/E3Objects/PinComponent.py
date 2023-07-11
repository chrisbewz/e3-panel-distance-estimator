from dependency_injector.wiring import Provide, inject

from ...BaseTypes.Handlers.PinBase import PinBase
from ...Extensions.Mappers import AbstractMapper
from ...Implementations.E3Objects.ComponentSchemas import PinSchema
from ...BaseTypes.Enumerations.Pin import PIN_PLACEMENT, PIN_SIDE, PIN_DIRECTIONS, PIN_CONNECTION_KIND, \
    PIN_CAVITY_KIND, \
    PIN_END_KIND, PIN_NODE_KIND, PIN_TYPES
from ...Implementations.E3Objects.ComponentPositioning import PinPosition


class Pin(PinBase, AbstractMapper):
    _nets = None

    def __init__(self, pinId):
        super().__init__(pinId)

    @property
    def maxCrossSection(self) -> float:
        return super().GetPinPhysicalTotalMaxCrossSection()

    @property
    def minCrossSection(self):
        return super().GetPinPhysicalTotalMinCrossSection()

    @property
    def physicalPosition(self) -> (int, PinPosition):
        return super().GetPinPhysicalPosition()

    @property
    def pinTypeId(self) -> PIN_TYPES:
        return super().GetPinTypeId()

    @property
    def translateSignalName(self) -> str:
        return super().GetPinTranslatedSignalName()

    @property
    def location(self) -> PinSchema:
        return super().GetPinSchemaLocation()

    @property
    def wires(self) -> (int, tuple):
        return super().GetPinWiresPassed()

    @property
    def panelPath(self) -> (int, PinPosition):
        return super().GetPinPanelPath()

    @property
    def outerDiameter(self) -> int:
        return super().GetPinOuterDiameter()

    @property
    def destinations(self) -> (int, tuple):
        return super().GetPinDestinationIds()

    @property
    def signalName(self):
        return super().GetPinSignalName()

    @property
    def connectedIds(self):
        return super().GetPinConnectedIds()

    @property
    def netSegments(self):
        return super().GetPinNetSegmentIds()

    @property
    def isRouted(self):
        return super().CheckPinRouting()

    @property
    def connectionDirection(self):
        return super().GetPinPhysicalConnectionDirection()

    @property
    def cores(self):
        return super().GetPinCoreIds()

    @property
    def parent(self):
        return super().GetPinDeviceIds()

    @classmethod
    @inject
    def Create(cls, identifier: int, deviceInstance=Provide["interop"]):
        pass

    @inject
    def Map(self, destinations: (int, tuple), instance=Provide["interop"]) -> any:
        _pin_ref = instance.PinRef
        try:
            cout, dests = destinations
            if cout is 0:
                return {}

            for dest in dests:
                if dest is None:
                    continue

                _pin_id = _pin_ref.SetId(dest)

                if _pin_id > 0:
                    mapped = {

                        "name": _pin_ref.GetName(),
                        "segments": _pin_ref.GetNetSegmentIds(),
                        "nodes": _pin_ref.GetNodeIds(),
                        "devicePins": _pin_ref.GetDevicePinIds(),
                        "id": _pin_ref.GetId()
                    }
                    return mapped

        except:
            raise ValueError(f"Algo deu errado ao configurar o Id do pino")

    def DistanceTo(self, other):
        return self.physicalPosition[1].coordinates.__sub__(other.physicalPosition[1].coordinates)

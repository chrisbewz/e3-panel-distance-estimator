from dependency_injector.wiring import Provide

from ...Implementations.E3Objects.AttributeComponent import AttributeComponent
from ...Implementations.E3Objects.ComponentSchemas import PinSchema
from ...BaseTypes.Enumerations.Pin import PIN_PLACEMENT, PIN_SIDE, PIN_DIRECTIONS, PIN_CONNECTION_KIND, \
    PIN_CAVITY_KIND, \
    PIN_END_KIND, PIN_NODE_KIND, PIN_TYPES
from ...Implementations.E3Objects.ComponentPositioning import PinPosition
from ...BaseTypes.Contracts.ObjectBase import ObjectBase


class PinBase(ObjectBase):
    __pin_id: int = None
    __pin_instance = None
    __attributes: list[AttributeComponent] = []

    def __init__(self, identifier: int, instance=Provide["interop"]):
        self.__pin_id = identifier
        self.__pin_instance = instance.PinRef
        super().__init__()
        self.ConfigureInstance()

    def __configure_attributes(self) -> list[AttributeComponent]:
        _att_ref = self.GetReferenceFromContainer("AttRef")
        self.__pin_instance.SetId(self.__pin_id)
        _attributes: list[AttributeComponent] = []
        _att_count, _att_ids = self.__pin_instance.GetAttributeIds(self.__pin_id)

        for att in _att_ids:
            if not att is None:
                _att_ref.SetId(att)
                _attributes.append(AttributeComponent(att))

        return _attributes

    def ConfigureInstance(self):
        self.__attributes = self.__configure_attributes()

    def FindPinRoutingPath(self):
        self.__pin_instance.FindPanelPath()

    def GetPinCrossSection(self) -> float:
        return self.__pin_instance.GetCrossSection()

    def GetPinCrossSectionDescription(self) -> float:
        return self.__pin_instance.GetCrossSectionDescription()

    def GetPinConnectionType(self):
        return self.__pin_instance.GetConnectionType()

    def GetPinConnectionTypeDescription(self):
        return self.__pin_instance.GetConnectionTypeDescription()

    def GetPinFitting(self):
        return self.__pin_instance.GetFitting()

    def GetPinColour(self) -> int:
        return self.__pin_instance.GetColour()

    def GetPinAllNetSegmentIds(self, flags: int) -> (int, tuple, tuple, tuple, any):
        flags, views, types, viewCounts, ids = self._instance.GetAllNetSegmentIds(0)
        return flags, views, types, viewCounts, ids

    def GetPinNetSegmentIds(self) -> (int, list[int]):
        return self.__pin_instance.GetNetSegmentIds()

    def GetPinAllowMultipleWireCrimps(self):
        return self.__pin_instance.GetAllowMultipleWireCrimps()

    def GetPinCableDuctIds(self):
        return self.__pin_instance.GetCableDuctIds()

    def HighligthPin(self):
        return self.__pin_instance.HighLigth()

    def PinHasAttribute(self, name: str) -> bool:
        return self.__pin_instance.HasAttribute(name) is 1

    def GetPinValidFits(self):
        return self.__pin_instance.GetPinValidFittings()

    def GetPinWireKindId(self):
        return self.__pin_instance.GetWireKindId()

    def GetPinViewsCount(self):
        return self.__pin_instance.GetViewCount()

    def GetPinViewIds(self) -> (int, tuple):
        return self._instance.GetViewIds()

    def GetPinTypeId(self) -> PIN_TYPES:
        res = self.__pin_instance.GetTypeId()
        return PIN_TYPES(int(res))

    def GetPinTranslatedSignalName(self) -> str:
        return self.__pin_instance.GetTranslatedSignalName()

    def GetPinTextCount(self) -> int:
        return self.__pin_instance.GetTextCount()

    def GetPinTemplateSymbolIds(self):
        return self.__pin_instance.GetTemplateSymbolIds()

    def GetPinTemplateSymbolId(self):
        return self.__pin_instance.GetTemplateSymbolId()

    def GetPinSchemaLocation(self) -> PinSchema:
        refx = None
        refy = None
        grid = None
        col = None
        row = None

        result = self.__pin_instance.GetSchemaLocation(refx, refy, grid, col, row)

        return PinSchema(PIN_PLACEMENT(1), refx, refy, grid, col, row)

    def GetSchematicEndId(self, side: PIN_SIDE) -> int:
        return self.__pin_instance.GetSchematicEndPinId(side)

    def GetPinRelativePermittivity(self):
        return self.__pin_instance.GetRelativePermittivity()

    def GetPinPortName(self) -> str:
        return self.__pin_instance.GetPortName()

    def GetIndex(self) -> int:
        return self.__pin_instance.GetPinIndex()

    def GetPinPhysicalTotalMaxCrossSection(self) -> float:
        return self.__pin_instance.GetPhysicalTotalMaxCrossSection()

    def GetPinPhysicalPosition(self) -> (int, PinPosition):
        res, xPos, yPos, zPos = self.__pin_instance.GetPhysicalPosition()

        return (res, PinPosition(xPos, yPos, zPos))

    def GetPinPhysicalTotalMinCrossSection(self) -> float:
        return self.__pin_instance.GetPhysicalTotalMinCrossSection()

    def GetPinPhysicalConnectionDirection(self) -> PIN_DIRECTIONS:
        return PIN_DIRECTIONS(self.__pin_instance.GetPhysicalConnectionDirection())

    def GetPinPhysicalConnectionType(self) -> PIN_CONNECTION_KIND:
        return PIN_CONNECTION_KIND(self.__pin_instance.GetPhysicalConnectionType())

    def GetPinPhysicalConnectionTypeDescription(self) -> str:
        return self.__pin_instance.GetPhysicalConnectionTypeDescription()

    def GetPinPhysicalMaxConnections(self) -> int:
        return self.__pin_instance.GetPhysicalMaxConnections()

    def GetPinWiresPassed(self) -> (int, tuple):
        return self.__pin_instance.GetPassWires()

    def GetPassedPins(self) -> (int, tuple):
        return self.__pin_instance.GetPassPins()

    def GetPinPanelPath(self) -> (int, PinPosition):
        corners, xPos, yPos, zPos = self._instance.GetPanelPath()
        return (corners, PinPosition(xPos, yPos, zPos))

    def GetPinOverbraidId(self) -> int:
        return self.__pin_instance.GetOverbraidID()

    def GetPinOuterDiameter(self) -> int:
        return self.__pin_instance.GetOuterDiameter()

    def GetPinDefinedOuterDiameter(self) -> int:
        return self.__pin_instance.GetDefinedOuterDiameter()

    def DeletePin(self) -> int:
        return self.__pin_instance.Delete()

    def DeletePinPath(self) -> int:
        return self.__pin_instance.DeletePanelPath()

    def UpdatePinWireNames(self) -> int:
        return self.__pin_instance.GenerateNewWireNames([self._id])

    def GetPinAssignedOptIds(self) -> (int, tuple):
        return self.__pin_instance.GetAssignedOptionIds()

    def GetPinBlockConnectionNumber(self) -> int:
        return self.__pin_instance.GetBlockConnectionNumber()

    def GetPinCavityIds(self, kind: PIN_CAVITY_KIND):
        return self.__pin_instance.GetCavityPartIds(kind.value)

    def GetPinCCT(self):
        return self.__pin_instance.GetCCT()

    def GetPinColorDescription(self) -> str:
        return self.__pin_instance.GetColourDescription()

    def GetPinConnectedNodeIds(self) -> (int, tuple):
        return self.__pin_instance.GetConnectedNodeIds()

    def GetPinConnectedIds(self) -> (int, tuple):
        return self.__pin_instance.GetConnectedPinIds()

    def GetPinCoreIds(self) -> (int, tuple):
        return self.__pin_instance.GetCoreIds()

    def GetPinCoreManufacturingLength(self) -> int:
        return self.__pin_instance.GetCoreManufacturingLength()

    def GetPinCoreWeight(self) -> float:
        return self.__pin_instance.GetCoreWeight()

    def GetPinCoreCost(self) -> float:
        return self.__pin_instance.GetCoreCost()

    def GetPinDefaultWires(self) -> (int, any, any):
        return self.__pin_instance.GetDefaultWires()

    def GetPinDestinationIds(self) -> (int, tuple):
        return self.__pin_instance.GetDestinationIds()

    def GetPinDeviceIds(self) -> (int, tuple):
        return self.__pin_instance.GetDevicePinIds()

    def GetPinDiameter(self) -> int:
        return self.__pin_instance.GetDiameter()

    def GetPinDiameterDescription(self) -> str:
        return self.__pin_instance.GetDiameterDescription()

    def GetCoreEndPinId(self, flag: PIN_END_KIND):
        return self.__pin_instance.GetEndPinId(flag.value, 0)

    def GetCoreLength(self):
        return self.__pin_instance.GetLength()

    def SetCoreLength(self, value: float) -> any:
        res = self.__pin_instance.SetLength(value)
        return res

    def GetPinMaterial(self):
        return self.__pin_instance.GetMaterial()

    def GetPinMaterialDescription(self):
        return self._instance.GetMaterialDescription()

    def GetPinName(self):
        return self.__pin_instance.GetName()

    def SetPinName(self, name: str):
        return self.__pin_instance.SetName()

    def GetPinNodeIds(self) -> (int, tuple):
        return self.__pin_instance.GetNodeIds()

    def GetPinNodeType(self):
        return self.__pin_instance.GetNodeType()

    def GetPinSignalName(self) -> str:
        return self.__pin_instance.GetSignalName()

    def Route(self):
        return self.__pin_instance.FindPanelPath()

    def CheckPinRouting(self) -> bool:
        return True if self.__pin_instance.IsRouted() == 1 else False

    @property
    def pId(self):
        return self.__pin_id

    @property
    def pinHasDevice(self) -> bool:
        return self.__pin_instance.HasDevice() is 1

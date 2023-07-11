from dependency_injector.wiring import Provide, inject

from RouteEstimator.BaseTypes.Contracts.ObjectBase import ObjectBase
from RouteEstimator.Implementations.E3Objects.AttributeComponent import AttributeComponent
from RouteEstimator.Implementations.E3Objects.PinComponent import Pin


class NetSegmentBase(ObjectBase):
    __net_seg_id: int = None
    __net_seg_instance = None
    __segment_name: str = None
    __rotation = None
    __level: int = None
    __attributes: list[AttributeComponent] = []
    __bus_name: str = None
    __s_length: float = None
    __signalName: str = None

    @inject
    def __init__(self, identifier: int, instance=Provide["interop"]):
        self.__net_seg_id = identifier
        self.__net_seg_instance = instance.NetRef
        super().__init__()
        self.ConfigureInstance()

    def ConfigureInstance(self):

        self.__net_seg_instance.SetId(self.__net_seg_id)
        self.__segment_name = self.__net_seg_instance.GetName()
        # self.__rotation = self.__net_seg_instance.GetRotation()
        self.__level = self.__net_seg_instance.GetLevel()
        self.__bus_name = self.__net_seg_instance.GetBusName()
        self.__s_length = self.__net_seg_instance.GetSchemaLength()
        self.__signalName = self.__net_seg_instance.GetSignalName()
        self.__configure_attributes()

    def __configure_attributes(self):
        _attributes: list[AttributeComponent] = []
        _att_count, _att_ids = self.__net_seg_instance.GetAttributeIds(self.__net_seg_id)

        for att in _att_ids[1:]:
            self.__attributes.append(AttributeComponent(att))

    @property
    def name(self) -> str:
        return self.__segment_name
    
    @property
    def busName(self) -> str:
        return self.__bus_name
    
    @property
    def id(self) -> int:
        return self.__net_seg_id

    @property
    def attributes(self) -> list[AttributeComponent]:
        return self.__attributes

    @property
    def level(self) -> int:
        return self.__level

    @property
    def rotation(self) -> float:
        return self.__rotation

    @property
    def schemaLength(self) -> float:
        return self.__s_length

    @property
    def signalName(self) -> str:
        return self.__signalName

    @property
    def isPanelPath(self) -> bool:
        return self.__net_seg_instance.IsPanelPath() is 1

    @property
    def isBus(self) -> bool:
        return self.__net_seg_instance.IsBus() is 1

    @property
    def isOffLine(self) -> bool:
        return self.__net_seg_instance.IsOffline() is 1

    @property
    def isView(self) -> bool:
        return self.__net_seg_instance.IsView() is 1
    





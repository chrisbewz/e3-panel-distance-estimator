from dependency_injector.wiring import Provide

from RouteEstimator.BaseTypes.Contracts.ObjectBase import ObjectBase
from RouteEstimator.BaseTypes.Handlers.NetSegmentBase import NetSegmentBase
from RouteEstimator.Implementations.E3Objects.AttributeComponent import AttributeComponent


class ConnectionBase(ObjectBase):
    __conn_id: int = None
    __conn_instance = None
    __attributes: list[AttributeComponent] = []
    __cores: list = []
    __net_segments: list[NetSegmentBase] = []
    __connection_net_id: int = None

    def __init__(self, identifier: int, instance=Provide["interop"]):
        self.__conn_instance = instance.ConnRef
        self.__conn_id = identifier
        super().__init__()
        self.ConfigureInstance()

    def ConfigureInstance(self):
        self.__conn_instance.SetId(self.__conn_id)
        self.__configure_signals()
        self.__configure_attributes()
        self.__configure_core_information()

    def __configure_attributes(self):
        _att_count, _att_ids = self.__conn_instance.GetAttributeIds()
        for att in _att_ids[1:]:
            self.__attributes.append(AttributeComponent(att))

    def __configure_core_information(self):
        self.__connection_net_id = self.__conn_instance.GetNetId()

    def __configure_signals(self):
        pass

    @property
    def cores(self):
        return self.__cores

    @property
    def id(self):
        return self.__conn_id

    @property
    def attributes(self):
        return self.__attributes

    @property
    def netSegments(self):
        return self.__net_segments

    @property
    def connectionNetId(self):
        return self.__connection_net_id

    @property
    def isValid(self):
        return self.__conn_instance.IsValid()

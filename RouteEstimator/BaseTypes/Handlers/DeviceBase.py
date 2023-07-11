from ...Implementations.E3Objects.AttributeComponent import AttributeComponent
from ...Implementations.E3Objects.PinComponent import Pin
from ...BaseTypes.Contracts.ObjectBase import ObjectBase
from dependency_injector.wiring import Provide, inject


class DeviceBase(ObjectBase):

    __instance = None
    __device_id: int = None
    __name: str = None
    __location: any = None
    __assembly: str = None
    __pins: list[Pin] = None
    __attributes: list[AttributeComponent] = []

    def __init__(self, identifier: int, instance=Provide["interop"]):
        self.__instance = instance.DeviceRef
        self.__device_id = identifier
        super().__init__()
        self.ConfigureInstance()

    def __configure_pins_(self) -> None:
        try:
            _pin_ref = self.GetReferenceFromContainer("PinRef")
            self.__instance.SetId(self.__device_id)
            pinCount, pinIds = self.__get_pin_ids_()
            self.__pins = [Pin(pid) for pid in pinIds if not pid is None]

        except:
            raise
    def __configure_attributes(self) -> list[AttributeComponent]:
        _att_ref = self.GetReferenceFromContainer("AttRef")
        self.__instance.SetId(self.__device_id)
        _attributes: list[AttributeComponent] = []
        _att_count, _att_ids = self.__instance.GetAttributeIds(self.__device_id)

        for att in _att_ids:
            if not att is None:
                _att_ref.SetId(att)
                _attributes.append(AttributeComponent(att))

        return _attributes
    def __get_pin_ids_(self) -> (int, int):
        pinsCount, pinIds = self.__instance.GetPinIds()
        return pinsCount, pinIds
    def ConfigureInstance(self):
        self.__instance.SetId(self.__device_id)
        self.__name = self.__instance.GetName()
        self.__location = self.__instance.GetLocation()
        self.__assembly = self.__instance.GetAssemblyId()
        self.__attributes = self.__configure_attributes()
        self.__configure_pins_()

    def AddDeviceAttribute(self, name: str, value: str) -> bool:
        try:
            self.__instance.AddAttribute(name, value)
            return True
        except:
            return False

    def AutoSolveDeviceStrip(self) -> None:
        self.__instance.AutoSolveStrip()

    def DeleteDevice(self) -> bool:
        try:
            self.__instance.Delete()
            return True
        except:
            return False

    def GetPinAt(self, index: int) -> Pin:
        return self.__pins[index]
    def GetDeviceNetIds(self):
        self.__instance.SetId(self.__device_id)
        return self.__instance.GetNetIds()
    def GetDeviceCoreIds(self):
        self.__instance.SetId(self.__device_id)
        return self.__instance.GetCoreIds()
    def GetDeviceCableIds(self):
        return self.__instance.GetCableIds()
    @property
    def pinCount(self) -> int:
        return len(self.__pins)
    @property
    def id(self):
        return self.__device_id
    @property
    def name(self):
        return self.__name
    @property
    def location(self):
        return self.__location
    @property
    def assemblyId(self):
        return self.__assembly
    @property
    def pins(self):
        return self.__pins
    @property
    def nets(self) -> (int, list[int]):
        return self.GetDeviceNetIds()
    @property
    def cores(self):
        return self.GetDeviceCoreIds()
    @property
    def cables(self):
        return self.GetDeviceCableIds()
    @property
    def attributes(self):
        return self.__attributes


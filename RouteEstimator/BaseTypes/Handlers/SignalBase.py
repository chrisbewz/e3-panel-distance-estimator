from dependency_injector.wiring import Provide, inject

from ...BaseTypes.Contracts.ObjectBase import ObjectBase
from ...Implementations.E3Objects.AttributeComponent import AttributeComponent


class SignalBase(ObjectBase):
    __signal_instance = None
    __signal_id: int = None
    __name: str = None
    __attributes: list[AttributeComponent] = []

    def __init__(self, identifier: int, instance=Provide["interop"]):
        self.__signal_id = identifier
        self.__signal_instance = instance.SignalRef
        super().__init__()
        self.ConfigureInstance()

    def ConfigureInstance(self):
        self.__signal_instance.SetId(self.__signal_id)
        self.__configure_attributes()
        self.__name = self.__signal_instance.GetName()

    def __configure_attributes(self):
        self.__signal_instance.SetId(self.__signal_id)
        _att_count, _att_ids = self.__signal_instance.GetAttributeIds(self.__signal_id)

        for att in _att_ids:
            if not att is None:
                self.__attributes.append(AttributeComponent(att))

    @staticmethod
    @inject
    def RemoveFromId(identifier: int, instance=Provide["interop"]) -> bool:
        return instance.SignalRef.RemoveSignalId(identifier) is 1

    @classmethod
    @inject
    def CreateClass(cls, name: str, instance=Provide["interop"]) -> bool:
        return instance.SignalRef.Create(name) is 1

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__signal_id

    @property
    def attributes(self):
        return self.__attributes


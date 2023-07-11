from dependency_injector.wiring import Provide

from RouteEstimator.BaseTypes.Contracts.ObjectBase import ObjectBase


class AttributeBase(ObjectBase):
    __att_id = None
    __value = None
    __name: str = None
    __text_ids: list[int] = None
    __owner_id: int = None
    __formatted_value = None
    __instance = None

    def __init__(self, identifier: int, instance=Provide["interop"]):
        self.__instance = instance.AttRef
        self.__att_id = identifier
        super().__init__()
        self.ConfigureInstance()

    def ConfigureInstance(self):
        try:
            self.__instance.SetId(self.__att_id)
            self.__value = self.__instance.GetValue()
            self.__name = self.__instance.GetName()
            self.__formatted_value = self.__instance.GetFormattedValue()

        except:
            raise

    @property
    def value(self):
        return self.__value

    @property
    def name(self):
        return self.__name

    @property
    def formattedValue(self):
        return self.__formatted_value

    @property
    def owner(self):
        return self.__owner_id

    @property
    def textIds(self) -> list[int]:
        return self.__text_ids

    @property
    def instance(self):
        return self.__instance

    @staticmethod
    def MapFromParent(parentId: int, instance=Provide["interop"]) -> list:
        from ...Implementations.E3Objects.AttributeComponent import AttributeComponent as att
        _att_ref = instance.AttRef
        _id_set = _att_ref.SetId(parentId)
        if _id_set > 0:
            return [att(_p_id) for _p_count, _p_id in _att_ref.GetAttributeIds() if not _p_count is 0]

        return []

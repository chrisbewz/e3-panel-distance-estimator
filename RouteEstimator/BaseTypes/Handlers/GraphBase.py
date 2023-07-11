from dependency_injector.wiring import Provide

from RouteEstimator.BaseTypes.Contracts.ObjectBase import ObjectBase
from RouteEstimator.Implementations.E3Objects.AttributeComponent import AttributeComponent


class GraphBase(ObjectBase):
    __graph_instance: any = None
    __attributes: list[AttributeComponent] = []
    __parent_id: int = None
    __graph_id: int = None
    __name: str = None

    def __init__(self, identifier: int, instance=Provide["interop"]):
        super().__init__()
        self.__graph_instance = instance.GraphRef
        self.__graph_id = identifier
        self.ConfigureInstance()

    def ConfigureInstance(self):
        try:
            self.__graph_instance.SetId(self.__graph_id)
            self.__parent_id = self.__get_parent()
            self.__attributes = AttributeComponent.MapFromParent(self.__parent_id)

        except:
            raise

    def __get_parent(self) -> int:
        _gp_id = self.__graph_instance.SetId(self.__graph_id)
        if _gp_id > 0:
            return self.__graph_instance.GetParentId()
        return 0

    @property
    def instance(self):
        return self.__graph_instance

    @property
    def id(self):
        return self.__graph_id

    @property
    def attributes(self):
        return self.__attributes

    @property
    def parent(self):
        return self.__parent_id

from dependency_injector.wiring import Provide

from RouteEstimator.BaseTypes.Contracts.AreaBase import AreaBase
from RouteEstimator.BaseTypes.Contracts.ObjectBase import ObjectBase
from RouteEstimator.BaseTypes.Enumerations.Symbol import SYMBOL_CODES, SYMBOL_STATE
from RouteEstimator.BaseTypes.Models.SymbolStyleModel import SymbolStyle
from RouteEstimator.Implementations.E3Objects.AttributeComponent import AttributeComponent
from RouteEstimator.Implementations.E3Objects.ComponentSchemas import SymbolSchema


class SymbolBase(ObjectBase):
    __symbol_id: int = None
    __symbol_instance = None
    __attributes: list[AttributeComponent] = []
    __children_symbols: list = []
    __placed_poligons = None
    __symbol_style: SymbolStyle = None
    __code: SYMBOL_CODES = None
    __display_length: float = None
    __display_width: float = None
    __level: int = None
    __name: str = None
    __scale: any = None
    __schema_location: SymbolSchema = None
    __placed_area: AreaBase = None
    __area: AreaBase = None
    __version: str = None
    __graphic_state: SYMBOL_STATE = None
    __has_wires_attached: bool = False

    def __init__(self, identifier: int, instance=Provide["interop"]):
        self.__symbol_id = identifier
        self.__symbol_instance = instance.SymbolRef
        super().__init__()
        self.ConfigureInstance()

    def ConfigureInstance(self):
        self.__symbol_instance.SetId(self.__symbol_id)
        self.__display_length = self.__symbol_instance.GetDisplayLength()
        self.__display_width = self.__symbol_instance.GetDisplayWidth()
        self.__configure_attributes()
        self.__configure_schema()
        self.__configure_areas()
        self.__check_graphics_state()
        self.__code = self.__configure_code()
        self.__level = self.__symbol_instance.GetLevel()
        self.__name = self.__symbol_instance.GetName()
        self.__scale = self.__symbol_instance.GetScaling()
        self.__version = self.__symbol_instance.GetVersion()

    def __configure_attributes(self):
        self.__symbol_instance.SetId(self.__symbol_id)
        _att_count, _att_ids = self.__symbol_instance.GetAttributeIds(self.__symbol_id)
        for att in _att_ids:
            if not att is None:
                self.__attributes.append(AttributeComponent(att))

    def __check_graphics_state(self) -> SYMBOL_STATE:
        return SYMBOL_STATE(self.__symbol_instance.HasNoGraphic())

    def __check_wire_refs(self):
        self.__has_wires_attached = self.__symbol_instance.HasPassWirePins()
    def __configure_schema(self):
        _res, _x, _y, _grid, _col, _row = self.__symbol_instance.GetSchemaLocation()
        self.__schema_location = SymbolSchema(_x, _y, _grid, _col, _row)

    def __configure_areas(self):
        _res_placed, _placed_area_xmin, _placed_area_ymin, _placed_area_xmax, _placed_area_ymax = self.__symbol_instance.GetPlacedArea()
        _res_main, _main_area_xmin, _main_area_ymin, _main_area_xmax, _main_area_ymax = self.__symbol_instance.GetArea()

        self.__placed_area = AreaBase(_placed_area_xmax, _placed_area_xmin, _placed_area_ymax, _placed_area_ymin)
        self.__area = AreaBase(_main_area_xmax, _main_area_xmin, _main_area_ymax, _main_area_ymin)

    def __configure_code(self) -> SYMBOL_CODES:
        return SYMBOL_CODES(self.__symbol_instance.GetCode())

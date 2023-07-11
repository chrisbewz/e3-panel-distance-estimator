from dependency_injector.wiring import Provide

from RouteEstimator.BaseTypes.Contracts.ObjectBase import ObjectBase
from ...BaseTypes.Models.DimensionStyleModel import DimensionStyle


class DimensionBase(ObjectBase):
    __dimension_id: int = None
    __attributes: list = []
    __text: str = None
    __linew: float = None
    __level: int = None
    __is_redlined: bool = False
    __is_along_path: bool = False
    __prefix: str = None
    __style: DimensionStyle = None
    __dimension_instance = None

    def __init__(self, identifier: int, instance=Provide["interop"]):
        super().__init__()
        self.__dimension_instance = instance.DimensionRef
        self.__dimension_id = identifier
        self.ConfigureInstance()

    def ConfigureInitialInstance(self):
        try:
            self.__dimension_instance.SetId(self.__dimension_id)
            self.__prefix = self.__dimension_instance.GetPrefix()
            self.__text = self.__dimension_instance.GetText()
            self.__linew = self.__dimension_instance.GetLineWidth()
            self.__level = self.__dimension_instance.GetLevel()
            self.__check_along()
            self.__check_redlines()
            self.__style = self.__configure_style()
        except:
            raise

    def __configure_style(self) -> DimensionStyle:
        _txt_style = self.__dimension_instance.GetTextStyle()
        _color = self.__dimension_instance.GetTextColour()
        _font_name = self.__dimension_instance.GetFontName()
        _height = self.__dimension_instance.GetTextHeight()
        _suffix = self.__dimension_instance.GetSuffix()
        _prefix = self.__dimension_instance.GetPrefix()
        _offset = self.__dimension_instance.GetOffset()

        return DimensionStyle(_font_name, _color, _height, _txt_style, _offset, _prefix, _suffix)


    def __check_along(self):
        self.__dimension_instance.SetId(self.__dimension_id)
        _is_along = self.__dimension_instance.IsAlongPath()
        return _is_along

    def __check_redlines(self):
        self.__dimension_instance.SetId(self.__dimension_id)
        _is_redline = self.__dimension_instance.IsRedlined()
        return _is_redline


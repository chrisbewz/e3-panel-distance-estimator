from RouteEstimator.BaseTypes.Enumerations.Text import TEXT_STYLE
from RouteEstimator.BaseTypes.Misc.ColorFormats import RgbColor


class DimensionStyle:
    __font_name: str = None
    __font_color: RgbColor = None
    __text_height: float = None
    __text_style: TEXT_STYLE = TEXT_STYLE.NEW
    __text_offset: float = None
    __prefix: str = None
    __suffix: str = None

    def __init__(self, font, color, height, textStyle: TEXT_STYLE, offset, prefix, suffix):
        self.__font_color = color
        self.__text_height = height
        self.__font_name = font
        self.__text_style = textStyle
        self.__text_offset = offset
        self.__prefix = prefix
        self.__suffix = suffix

    @property
    def fontName(self) -> str:
        return self.__font_name

    @property
    def color(self) -> RgbColor:
        return self.__font_color

    def height(self) -> float:
        return self.__text_height

    @property
    def prefix(self) -> str:
        return self.__prefix

    @property
    def suffix(self) -> RgbColor:
        return self.__suffix

    def offset(self) -> float:
        return self.__text_offset

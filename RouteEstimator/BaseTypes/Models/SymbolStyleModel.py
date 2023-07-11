import dataclasses

from RouteEstimator.BaseTypes.Misc.ColorFormats import RgbColor


@dataclasses.dataclass
class SymbolStyle:

    __block_hatch_color: RgbColor = None
    __block_hatch_distance: float = None
    __block_hatch_style = None
    __block_hatch_width = None
    __block_outline_color: RgbColor = None
    __has_outline_color: bool = False
    __block_outline_style = None
    __block_outline_width = None

    def __init__(self, hatchColor: RgbColor, hatchDistance, hatchStyle, hatchWidth, outlineColor: RgbColor,
                 outlineStyle, outlineWidth):

        self.__block_outline_style = outlineStyle
        self.__block_outline_width = outlineWidth
        self.__block_hatch_style = hatchStyle
        self.__block_outline_color = outlineColor
        self.__block_hatch_color = hatchColor
        self.__block_hatch_distance = hatchDistance
        self.__block_hatch_width = hatchWidth

    @property
    def hatchColor(self):
        return self.__block_hatch_color
    @property
    def hatchDistance(self):
        return self.__block_hatch_distance
    @property
    def hatchWidth(self):
        return self.__block_hatch_width
    @property
    def hatchStyle(self):
        return self.__block_hatch_style
    @property
    def outlineColor(self):
        return self.__block_outline_color
    @property
    def outlineStyle(self):
        return self.__block_outline_style
    @property
    def outlineWidth(self):
        return self.__block_outline_width
    @property
    def hasOutlineColor(self):
        return self.__has_outline_color



from ...BaseTypes.Contracts.ColorBase import ColorBase


class RgbBase(ColorBase):
    _r: int = None
    _g: int = None
    _b: int = None

    def __init__(self, red: int, green: int, blue: int):
        self._r = red
        self._g = green
        self._b = blue

    @classmethod
    def Factory(cls):
        return cls(0,0,0)

    @property
    def red(self):
        return self._r

    @property
    def gree(self):
        return self._g

    @property
    def blue(self):
        return self._b

    def Value(self) -> (int,int,int):
        return self._r,self._g,self._b

from ...BaseTypes.Contracts.RgbBase import RgbBase


class RgbColor(RgbBase):

    def __init__(self, red: int, green: int, blue: int):
        super().__init__(red, green, blue)

from dependency_injector.wiring import Provide
from multipledispatch import dispatch

from ...BaseTypes.Handlers.SheetBase import *


class SheetComponent(SheetBase):

    def __init__(self, sheetId):
        super().__init__(sheetId)

    @classmethod
    @dispatch(object, int)
    def Create(cls, identifier: int):
        return cls(identifier)

    @classmethod
    @dispatch(object, str)
    def Create(cls, name: str):
        _sheet_result = None
        _sheet_obj = cls.GetReferenceFromContainer("SheetRef")
        _id_found = _sheet_obj.Search(0, name)
        if _id_found > 0:
            return cls(_id_found)
        else:
            return cls(None)

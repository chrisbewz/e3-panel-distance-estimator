from RouteEstimator.BaseTypes.Contracts.ObjectBase import ObjectBase
from RouteEstimator.Implementations.E3Objects.SheetComponent import SheetComponent


class JobBase:
    __job_instance = None
    __instance = None
    __sheets: list[SheetComponent] = []

    def __init__(self, instance):
        self.__instance = instance
        self.__job_instance = self.__instance.job

    def GetSelected(self) -> (int, list[int]):
        return self.__job_instance.GetSelectedDeviceIds()

    def GetSheetsInformation(self) -> None:
        _sheet_count, _sheet_ids = self.__job_instance.GetSheetIds()
        if _sheet_count != 0:
            for _sheet in _sheet_ids:
                if not _sheet is None:
                    self.__sheets.append(SheetComponent(_sheet))

    @property
    def jobInstance(self):
        return self.__job_instance

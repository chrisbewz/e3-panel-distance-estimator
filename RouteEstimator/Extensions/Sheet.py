from dependency_injector.wiring import inject, Provide


class SheetExtensions:

    @staticmethod
    @inject
    def ImportDrawing(sheetId: int, file: str, fontName, posX: float, posY: float, scale: float = 1.0, rotation: float = 0,
                      instance=Provide["interop"]):
        _sht_instance = instance.SheetRef
        _sht_instance.SetId(sheetId)
        region_info = SheetExtensions.GetRegionDetails()

        if scale > region_info[2]:
            raise ValueError(f"A escala da folha deve ser maior do que a escala de importação selecionada. Escala selecionada [{scale}] | Disponível : [{region_info[2]}]")

        _sht_instance.ImportDxf(file, scale, posX, posY, rotation, fontName, 0)

    @staticmethod
    @inject
    def GetRegionDetails(sheetId: int, instance=Provide["interop"]) -> (float, float, float):
        _sht_instance = instance.SheetRef
        _sht_instance.SetId(sheetId)
        return _sht_instance.GetSheetRegion()

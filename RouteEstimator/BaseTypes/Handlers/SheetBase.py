from dependency_injector.wiring import Provide

from ..Models.DrawingAreaModel import DrawingArea
from ...BaseTypes.Enumerations.Alignment import *
from ...BaseTypes.Enumerations.Sheet import *
from ...BaseTypes.Contracts.ObjectBase import ObjectBase
from ...Implementations.E3Objects.AttributeComponent import AttributeComponent
from ...Implementations.E3Objects.DimensionComponent import DimensionComponent
from ...Implementations.E3Objects.GraphComponent import GraphComponent
from ...Implementations.E3Objects.NetSegmentComponent import NetSegmentComponent
from ...Implementations.E3Objects.SymbolComponent import SymbolComponent


class SheetBase(ObjectBase):
    __sheet_name: str = None
    __sheet_id: int = None
    __sheet_attributes: list[AttributeComponent] = []
    __graphs: list[GraphComponent] = []
    __sheet_instance = None
    __current_drawing_area: DrawingArea = None
    __net_segments: list[NetSegmentComponent] = []
    __symbols: list[SymbolComponent] = []

    def __init__(self, identifier: int, instance=Provide["interop"]):
        super().__init__()
        self.__sheet_id = identifier
        self.__sheet_instance = instance.SheetRef
        self.ConfigureInstance()

    def ConfigureInstance(self):
        try:
            _id_set = self.__sheet_instance.SetId(self.__sheet_id)
            if not _id_set > 0:
                raise ValueError

            self.__sheet_attributes = self.__configure_attributes()
            self.__configure_names()
            self.__current_drawing_area = self.__get_drawing_area()
            self.__graphs = self.__get_contained_graphs()
            self.__get_net_segments()
            self.__setup_symbols()

        except ValueError:
            print("O identificador da folha não pode ser configurado")

    def AlignSelected(self, referenceId, targetIds, mode: ALIGN_DIRECTIONS):
        return ALIGNMENT_RESULT(self.__sheet_instance.AlignObjects(referenceId, targetIds, mode.value))

    def CreateNewSheet(self, name: str, symbol: str, idx: int, before: SHEET_POSITION) -> int:
        return self.__sheet_instance.Create(0, name, symbol, idx, before.value)

    def GetCurrentSheetDimensions(self):
        return self.__sheet_instance.GetDimensionIds()

    def GetCurrentSheetDisplay(self):
        return self.__sheet_instance.GetDisplay()

    def GetSheetFormatName(self):
        return self.__sheet_instance.Getformat()

    def GetSheetGraphIds(self):
        return self.__sheet_instance.GetGraphIds()

    def GetSheetGroupIds(self):
        return self.__sheet_instance.GetGroupIds()

    def GetSheetHyperlinkTextIds(self):
        return self.__sheet_instance.GetHyperlinkTextIds()

    def GetSheetContainedGraphicIds(self):
        return self.__sheet_instance.GetInsideGraphIds()

    def GetSheetContainedNetSegmentIds(self):
        self.__sheet_instance.GetInsideNetSegmentIds()

    def GetPanelConnectionsContained(self):
        self.__sheet_instance.GetInsidePanelConnectionIds()

    def GetContainedSymbolIds(self):
        return self.__sheet_instance.GetInsideSymbolIds()

    def GetSheetLocation(self):
        return self.__sheet_instance.GetLocation()

    def GetContainedModuleIds(self):
        return self.__sheet_instance.GetModuleIds()

    def GetSheetName(self):
        return self.__sheet_instance.GetName()

    def GetContainedNetIds(self):
        return self.__sheet_instance.GetNetIds()

    def GetContainedNetSegmentIds(self):
        return self.__sheet_instance.GetNetSegmentIds()

    def GetSheetOwner(self):
        return self.__sheet_instance.GetOwner()

    def GetSheetConnectionIds(self):
        return self.__sheet_instance.GetPanelConnectionIds()

    def GetSheetPanelRegion(self):
        return self.__sheet_instance.GetPanelRegion()

    def __configure_attributes(self) -> list[AttributeComponent]:
        _sht_ref = self.GetReferenceFromContainer("SheetRef")
        _sht_ref.SetId(self.__sheet_id)
        _attributes: list[AttributeComponent] = []
        _att_count, _att_ids = self.__sheet_instance.GetAttributeIds(_sht_ref)

        for att in _att_ids:
            if not att is None:
                _attributes.append(AttributeComponent(att))

        return _attributes

    def __configure_names(self) -> None:
        if not self.__sheet_id is 0 or self.__sheet_id is None:
            self.__sheet_instance.SetId(self.__sheet_id)
            self.__sheet_name = self.__sheet_instance.GetName()

    def __get_drawing_area(self) -> DrawingArea:
        self.__sheet_instance.SetId(self.__sheet_id)
        _res, _xmi, _ymi, _xma, _yma = self.__sheet_instance.GetDrawingArea()
        _draw_area = DrawingArea(_xma, _xmi, _yma, _ymi)
        return _draw_area

    def __get_visible_area(self) -> DrawingArea:
        self.__sheet_instance.SetId(self.__sheet_id)
        _res, _xmi, _ymi, _xma, _yma = self.__sheet_instance.GetVisibleArea()
        _vis_area = DrawingArea(_xma, _xmi, _yma, _ymi)
        return _vis_area

    def __get_contained_graphs(self) -> list[GraphComponent]:
        _gp_results: list[GraphComponent] = []
        self.__sheet_instance.SetId(self.__sheet_id)
        _gp_ref = self.GetReferenceFromContainer("GraphRef")
        _gp_count, _gp_ids = self.__sheet_instance.GetInsideGraphIds()

        if not _gp_count is 0:
            for _gp_id in _gp_ids:
                if not _gp_id is None:
                    _gp_ref.SetId(_gp_id)
                    _gp_results.append(GraphComponent(_gp_id))

        return _gp_results


    def __get_inner_dimensions_(self) -> list[DimensionComponent]:
        self.__sheet_instance.SetId(self.__sheet_id)
        _dim_ref = self.GetReferenceFromContainer("DimRef")
        _dim_contained: list[DimensionComponent] = []

        _dim_count, _dim_ids = self.__sheet_instance.GetDimensionIds()
        for dim in _dim_ids:
            if not dim is None:
                _dim_contained.append(DimensionComponent(dim))

        return _dim_contained

    def __get_net_segments(self):
        self.__sheet_instance.SetId(self.__sheet_id)
        _net_count, _net_ids = self.__sheet_instance.GetNetSegmentIds()

        for net in _net_ids:
            if net is not None:
                self.__net_segments.append(NetSegmentComponent(net))

    def __setup_symbols(self):
        self.__sheet_instance.SetId(self.__sheet_id)
        _sht_smb_id_count, _sht_smb_ids = self.__sheet_instance.GetSymbolIds()

        if _sht_smb_id_count is 0:
            return

        for _sheet_symbol in _sht_smb_ids:
            if not _sheet_symbol is None:
                self.__symbols.append(SymbolComponent(_sheet_symbol))


















from dependency_injector.wiring import inject, Provide


class SymbolExtensions:

    @staticmethod
    @inject
    def GetPinsFromSymbolReference(symbolId: int,instance=Provide["interop"]) -> list:
        from ..Implementations.E3Objects.PinComponent import Pin
        results: list[Pin] = []
        _smb_ref = instance.SymbolRef
        try:
            _smb_ref.SetId(symbolId)
            _pin_count, _pin_ids = _smb_ref.GetDevicePinIds()

            for _pin in _pin_ids:
                if not _pin is None:
                    results.append(Pin(_pin))

            return results

        except:
            raise

    @staticmethod
    @inject
    def ListDynamicChildrens(symbolId: int, instance=Provide["interop"]) -> list:
        from ..Implementations.E3Objects.SymbolComponent import SymbolComponent
        results: list[SymbolComponent] = []

        _smb_ref = instance.SymbolRef
        _smb_ref.SetId(symbolId)
        _chd_count, _chd_ids = _smb_ref.GetDynamicChildrenIds()
        for chd in _chd_ids:
            if not chd is None:
                results.append(SymbolComponent(chd))

        return results

    @staticmethod
    @inject
    def GetGroupId(symbolId: int, instance=Provide["interop"]):

        _smb_ref = instance.SymbolRef
        _smb_ref.SetId(symbolId)
        _gp_count, _gp_ids = _smb_ref.GetGroupId()

        if not _gp_count is 0:
            return _gp_ids

        return 0

    @staticmethod
    def JumpTo(symbolId: int, instance=Provide["interop"]):
        _smb_ref = instance.SymbolRef
        _smb_ref.SetId(symbolId)
        _smb_ref.Jump()



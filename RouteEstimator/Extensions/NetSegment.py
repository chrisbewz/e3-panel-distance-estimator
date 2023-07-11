from dependency_injector.wiring import inject, Provider


class NetSegmentExtensions:

    @staticmethod
    @inject
    def GetSignalIds(netSegmentId: int, instance=Provider["interop"]) -> list:
        _net_ref = instance.NetRef
        _net_ref.SetId(netSegmentId)
        _signal_id_count, _signal_ids = _net_ref.GetSignalIds()

        return _signal_ids

    @staticmethod
    @inject
    def GetSignals(netSegmentId: int, instance=Provider["interop"]) -> list:
        from ..Implementations.E3Objects.SignalComponent import SignalComponent
        results: list[SignalComponent] = []
        _net_ref = instance.NetRef
        _net_ref.SetId(netSegmentId)
        _signal_id_count, _signal_ids = _net_ref.GetSignalIds()
        for signal in _signal_ids:
            if not signal is None:
                results.append(SignalComponent(signal))

        return results

    @staticmethod
    @inject
    def GetNodes(netSegmentId: int, instance=Provider["interop"]) -> list:
        from ..Implementations.E3Objects.PinComponent import Pin
        results: list[Pin] = []
        _net_ref = instance.NetRef
        _net_ref.SetId(netSegmentId)
        _placed_pins_count, _pin_ids = _net_ref.GetNodeIds()
        for pin in _pin_ids:
            if not pin is None:
                results.append(Pin(pin))

        return results

    @staticmethod
    @inject
    def GetSymbolIds(netSegmentId: int, instance=Provider["interop"]) -> list:
        from ..Implementations.E3Objects.SymbolComponent import SymbolComponent
        results: list[SymbolComponent] = []
        _net_ref = instance.NetRef
        _net_ref.SetId(netSegmentId)
        _placed_pins_count, _pin_ids = _net_ref.GetSymbolIds()
        for smb in _pin_ids:
            if not smb is None:
                results.append(SymbolComponent(smb))

        return results

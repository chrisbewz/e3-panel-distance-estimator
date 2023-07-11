from ..Contracts.ApplicationBase import Application
from ...BaseTypes.Contracts.ReferenceBase import ReferenceBase
from dependency_injector import containers, providers
from ..Handlers.DispatcherBase import Dispatcher
from ...Implementations.E3Objects.JobComponent import Job


class E3InteropReferences(ReferenceBase):
    _pinObj = None
    _symbolObj = None
    _shtObj = None
    _deviceObj = None
    _graphObj = None
    _coreRef = None
    _connObj = None
    _netObj = None
    _attObj = None

    def __init__(self, instance: any):
        super().__init__(instance)

    @property
    def AttRef(self):
        return self.job.CreateAttributeObject()

    @property
    def PinRef(self):
        return self.job.CreatePinObject()

    @property
    def NetRef(self):
        return self.job.CreateNetSegmentObject()

    @property
    def CoreRef(self):
        return self.job.CreateCoreObject()

    @property
    def GraphRef(self):
        return self.job.CreateGraphObject()

    @property
    def DimensionRef(self):
        return self.job.CreateDimensionObject()

    @property
    def SymbolRef(self):
        return self.job.CreateSymbolObject()

    @property
    def DeviceRef(self):
        return self.job.CreateDeviceObject()

    @property
    def SheetRef(self):
        return self.job.CreateSheetObject()

    @property
    def ConnRef(self):
        return self.job.CreateConnectionObject()

    @property
    def SignalRef(self):
        return self.job.CreateSignalObject()


class ReferenceContainer(containers.DeclarativeContainer):

    dispatcher = providers.Singleton(Dispatcher)
    application = providers.Singleton(Application, instance=dispatcher)
    interop = providers.Singleton(E3InteropReferences, instance=application)
    currentJob = providers.Singleton(Job, job=interop)


from dependency_injector.wiring import Provide, inject
from ...BaseTypes.Handlers.DeviceBase import DeviceBase


class Device(DeviceBase):

    def __init__(self, iden: int):
        super().__init__(iden)

    @classmethod
    def __factoryCreate(cls, identifier):
        return cls(identifier)

    @classmethod
    @inject
    def Create(cls, identifier: int, deviceInstance=Provide["interop"]):
        clsObj = cls.__factoryCreate(identifier)
        mapping = clsObj.Map(identifier)
        return mapping

    @inject
    def Map(self, identifier: int, instance=Provide["interop"]):
        _device_ref = instance.DeviceRef
        try:
            if identifier is None:
                return

            _dev_set = _device_ref.SetId(identifier)

            if _dev_set > 0:
                name = _device_ref.GetName()
                r = self.__factoryCreate(_device_ref.GetId())
                return r

        except:
            raise

        finally:
            # clsObj.DisposeIdEx()
            pass

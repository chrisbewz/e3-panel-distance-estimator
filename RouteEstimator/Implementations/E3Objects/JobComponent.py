from ...Implementations.E3Objects.DeviceComponent import Device
from ...Implementations.E3Objects.PinComponent import Pin
from ...BaseTypes.Contracts.JobBase import JobBase


class Job(JobBase):
    _deviceObj = None
    _pinObj = None
    _symbolObj = None
    _shtObj = None
    _attObj = None
    _devices: list[Device] = []

    def __init__(self, job):
        super().__init__(job)

    @property
    def devices(self):
        return self._devices

    def ReadProjectDeviceIds(self):

        count, ids = self.jobInstance.GetAllDeviceIds()
        if count != 0:
            self._devices = [self.CreateDeviceFromId(id) for id in ids if id is not None]

    def GetInstance(self):
        return self.__instance

    def CreateDeviceFromId(self, identifier: int) -> Device:
        # return Device.Create(self.__instance.DeviceRef, identifier, False)
        return Device(identifier)

    def Add(self, devId: int):

        self._devices.append(self.CreateDeviceFromId(devId))

    def TryGetDevicePins(self, devId) -> list[Pin]:
        devPins: list[Pin] = []
        try:
            self._deviceObj.SetId(devId)
            pCout, pins = self._deviceObj.GetPinIds()

            for pin in pins:
                if not pin is None:
                    devPins.append(Pin(pin))

            return devPins

        except:
            raise

    @property
    def selectedDevices(self) -> list[Device]:
        selCount, selIds = super().GetSelected()
        devices = [self.CreateDeviceFromId(id) for id in selIds if id is not None]
        return devices

    @property
    def allDevices(self) -> list[Device]:
        if self._devices is None or len(self._devices) is 0:
            self.ReadProjectDeviceIds()
        return self._devices

    def Jump(self, id: int) -> int:
        return self.jobInstance.JumpToID(id)

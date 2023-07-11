from ...BaseTypes.Contracts.ApplicationBase import Application
from ...Implementations.E3Objects.JobComponent import Job


class Project(Application):
    _prj: Job = None
    _deviceIds = None

    def __init__(self, app: Application):
        self._prj = app.GetJobObject()
        self.SetProjectDeviceIds()

    def SetProjectDeviceIds(self):
        self._deviceIds = self._prj.ReadProjectDeviceIds()

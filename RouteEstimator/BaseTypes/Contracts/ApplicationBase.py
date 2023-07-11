from ...BaseTypes.Contracts.MessageBase import MessageBase
from ...BaseTypes.Models.MessageModel import MessageModel
from ...BaseTypes.Enumerations.Message import MSG_KIND
from ...BaseTypes.Contracts.ColorBase import ColorBase
from multipledispatch import dispatch


class Application(MessageBase):
    _instance = None
    _version = None

    def __init__(self, instance):
        super().__init__()
        self._instance = instance

    def GetInstance(self):
        return self._instance

    @property
    def GetVersion(self):
        return self._version

    def GetJobObject(self):
        return self._instance.ActiveInstance().CreateJobObject()

    @dispatch(MessageModel)
    def RaiseMessage(self, messageObj: MessageModel):
        if messageObj.kind == MSG_KIND.COMMOM:
            self._instance.ActiveInstance().PutMessage(messageObj.content)
        elif messageObj.kind == MSG_KIND.WARNING:
            self._instance.ActiveInstance().PutWarning(messageObj.hasFocus.value, messageObj.content)
        else:
            self._instance.ActiveInstance().PutError(messageObj.hasFocus.value, messageObj.content)

    @dispatch(str)
    def RaiseMessage(self, message: str):
        factory: MessageModel = MessageModel.Factory()
        if factory.kind == MSG_KIND.COMMOM:
            self._instance.ActiveInstance().PutMessage(message)
        elif factory.kind == MSG_KIND.WARNING:
            self._instance.ActiveInstance().PutWarning(factory.hasFocus.value, message)
        else:
            self._instance.ActiveInstance().PutError(factory.hasFocus.value, message)

    @dispatch(str, ColorBase)
    def RaiseMessage(self, message: str, colorObj: ColorBase):
        factory: MessageModel = MessageModel.Factory()
        if factory.kind == MSG_KIND.COMMOM:
            self._instance.ActiveInstance().PutMessageEx(factory.hasFocus.value, message, 0, colorObj.Value()[0],
                                                         colorObj.Value()[1], colorObj.Value()[2])
        elif factory.kind == MSG_KIND.WARNING:
            self._instance.ActiveInstance().PutWarningEx(factory.hasFocus.value, message, 0, colorObj.Value()[0],
                                                         colorObj.Value()[1], colorObj.Value()[2])
        else:
            self._instance.ActiveInstance().PutErrorEx(factory.hasFocus.value, message, 0, colorObj.Value()[0],
                                                       colorObj.Value()[1], colorObj.Value()[2])

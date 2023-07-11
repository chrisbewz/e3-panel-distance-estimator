from ...BaseTypes.Models.MessageModel import *
from abc import ABC, abstractmethod
from multipledispatch import dispatch
from ...BaseTypes.Contracts.ColorBase import ColorBase


class MessageBase(ABC):

    def __init__(self):
        pass

    @dispatch(MessageModel)
    @abstractmethod
    def RaiseMessage(self, messageObj: MessageModel):
        pass

    @dispatch(str)
    @abstractmethod
    def RaiseMessage(self, message):
        pass

    @dispatch(str, ColorBase)
    @abstractmethod
    def RaiseMessage(self, message, colorObj: ColorBase):
        pass

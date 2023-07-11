from ...BaseTypes.Enumerations.Message import MSG_KIND, MSG_AWAIT


class MessageModel:
    _content: str = None
    _kind: MSG_KIND = None
    _focusFlag: MSG_AWAIT = MSG_AWAIT.IGNORE

    def __init__(self, content: str = None, kind: MSG_KIND = MSG_KIND.COMMOM,prior:MSG_AWAIT = MSG_AWAIT.IGNORE):
        self._kind = kind
        self._content = content
        self._focusFlag = prior

    def SetContent(self, content: str):
        if not content == self._content:
            self._content = content

    def SetPriority(self, prior: MSG_AWAIT):
        self._focusFlag = prior

    def ClearContent(self):
        self._content = None

    @classmethod
    def Factory(cls):
        return cls("",MSG_KIND.COMMOM,MSG_AWAIT.IGNORE)
    @property
    def content(self):
        return self._content

    @property
    def kind(self):
        return self._kind

    @property
    def hasFocus(self):
        return self._focusFlag

    def __str__(self):
        return repr(dict(self))

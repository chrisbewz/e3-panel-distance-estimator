from multipledispatch import dispatch
from abc import ABC, abstractmethod, abstractclassmethod
from dependency_injector.wiring import (
    Provide, inject, provided, as_
)


class ObjectBase:

    _IdEx = None
    _id = None
    _instance = None

    def __init__(self):
        pass

    @property
    def __invoke__(self):
        if self._id is not None:
            self._instance.SetId(self._id)
        return self._instance

    @property
    def __invoke_id__(self):
        res = self._instance.SetId(self._id)
        return res, self._instance

    def __invoke_with_id(self):
        res = self._instance.SetId(self._IdEx)
        return res, self._instance

    def SetTempId(self, identifier):
        self._IdEx = identifier

    def DisposeIdEx(self):
        self._IdEx = None

    def ConfigureInitialId(self):
        pass

    @inject
    def GetReferenceFromContainer(self, refName: str, containerRef=Provide["interop"]):
        ref = getattr(containerRef, refName)
        return ref

    def SetInstance(self, value):
        self._instance = value

    @property
    def currentInstance(self):
        return self._instance

    def ConfigureInstance(self):
        pass

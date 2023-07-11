class ReferenceBase:
    _instance = None

    @staticmethod
    def Free(self, ref: any):
        ref = None

    def __init__(self, instance: any):
        self._instance = instance.GetInstance().ActiveInstance().CreateJobObject()

    @property
    def job(self):
        return self._instance

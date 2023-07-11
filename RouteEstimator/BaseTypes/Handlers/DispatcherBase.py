import win32com.client as comClient


class Dispatcher:

    activeInstance = None

    def __init__(self):
        self.CreateInstance()

    def CreateInstance(self):
        try:
            self.activeInstance = comClient.GetActiveObject('CT.Application')
        except:
            self.activeInstance = comClient.Dispatch('CT.Application')

    def ActiveInstance(self):
        return self.activeInstance
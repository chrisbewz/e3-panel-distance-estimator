from RouteEstimator.BaseTypes.Handlers.ConnectionBase import ConnectionBase


class ConnectionComponent(ConnectionBase):
    
    def __init__(self, identifier: int):
        super().__init__(identifier)



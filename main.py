import json

from RouteEstimator.BaseTypes.Contracts.ApplicationBase import Application
from RouteEstimator.BaseTypes.Handlers.DispatcherBase import Dispatcher
from RouteEstimator.Implementations.E3Objects.DeviceComponent import Device
from RouteEstimator.Implementations.E3Objects.JobComponent import Job
from RouteEstimator.BaseTypes.Handlers.RefereceManager import ReferenceContainer, E3InteropReferences
from RouteEstimator.Implementations.E3Objects.PinComponent import Pin
from RouteEstimator.EstimatorAlgorithm.Implementation import Estimator
import importlib.resources as res


def GetDistanceInformation(deviceList: list[Device]) -> list:
    results = []

    for device in deviceList:

        device_count = device.pinCount
        # appHndl.RaiseMessage(f"--------------------------")
        # appHndl.RaiseMessage(f"- Nome do Dispositivo - [{device.name}]")
        # appHndl.RaiseMessage(f"- Contagem de pinos: {device_count}")
        # appHndl.RaiseMessage(f"- Distâncias entre conexões:\n")

        for pin in device.pins:
            destination_count, destination_ids = pin.GetPinDestinationIds()

            if destination_ids is None or destination_count is 0:
                continue

            for destination in destination_ids:
                if destination is not None:
                    pp = Pin(destination)
                    cartesian_distance = pin.DistanceTo(pp)
                    destination_device = Device.Create(destination)
                    # appHndl.RaiseMessage(
                    #     f"- [{device.name} -> {destination_device.name}] - [{pin.pId}] <-> {destination}]\n"
                    #     f" - x: [{cartesian_distance.xPos / 100}]\n"
                    #     f" - y: [{cartesian_distance.yPos / 100}]\n"
                    #     f" - z: [{cartesian_distance.zPos / 100}]\n"
                    #     f" - Euclidiana : [{pin.physicalPosition[1].coordinates.EuclideanDistance(pp.physicalPosition[1].coordinates) / 100}]\n")

                    fetch = \
                        {
                            "main-device-name": device.name,
                            "main-device-ref": device,
                            "main-device-id": device.id,
                            "pin": {pin.pId},
                            "device-pin-destinations":
                                {
                                    destination:
                                    {
                                        "device-ref": destination_device,
                                        "device-name": destination_device.name,
                                        "destination-id": destination,

                                        "distance-to-parent":
                                        {
                                            "absolute":
                                                {
                                                    "x-position": cartesian_distance.xPos / 100,
                                                    "y-position": cartesian_distance.yPos / 100,
                                                    "z-position": cartesian_distance.zPos / 100,
                                                },
                                            "euclidean": pin.physicalPosition[1].coordinates.EuclideanDistance(pp.physicalPosition[1].coordinates) / 100
                                        },
                                    }
                                }
                            }

                    results.append(fetch)
        #
        #
        # appHndl.RaiseMessage(f"\n")
        return results

def ParseAttributeInformation(formatted:list):
    for device in formatted:
        pass


if __name__ == "__main__":

    # Just for tests if some action needs to be performed on a class
    # like a functional script this container refs can be injected through inject decorator
    container = ReferenceContainer()
    container.wire(modules=[__name__], packages=[
        "RouteEstimator.BaseTypes",
        "RouteEstimator.Implementations",
    ])

    #Initializing Estimator Algorithm
    # stm = Estimator()

    # Just in case that has a separate python package to wire as dependency to inject
    jobHandl: Job = container.currentJob()
    appHndl: Application = container.application()
    dispatchHndl: Dispatcher = container.dispatcher()
    e3DtoHndl: E3InteropReferences = container.interop()

    #gathering devices information for all project
    current_selected_devices = jobHandl.allDevices

    #fetching initial information about placed connections and distances
    fetch_information = GetDistanceInformation(current_selected_devices)

    #recurse fetch data finding desired attributes
    with open("RouteEstimator/Resources/ATT_CONFIG.json") as cfg:
        content = json.load(cfg)

    for device in fetch_information:
        p = device["main-device-ref"]
    print('q')

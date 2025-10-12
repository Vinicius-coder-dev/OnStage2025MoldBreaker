from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Color, Port
from pybricks.tools import wait

# Initialize the hub.
hub = PrimeHub(observe_channels=[1])
while True:
    data = hub.ble.observe(1)
    if data is not None:
        Adress, Command = data
        print(Adress, Command)
        wait(500)
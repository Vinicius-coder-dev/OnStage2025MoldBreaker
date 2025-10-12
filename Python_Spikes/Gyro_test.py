from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, Matrix, vector
PI = 3.1415
motorD = Motor(Port.E)
motorE = Motor(Port.F)


X = Matrix([[1,0,0]])
hub = PrimeHub()

hub.imu.settings(2.0, 2500.0, 360,(0.0, 0.0, 0.0), (367.35, 358.5, 360.38), (9806.65, -9806.65, 9806.65, -9806.65, 9806.65, -9806.65))
#print(hub.imu.settings())

def Angle(Angle_target):
    hub.imu.reset_heading(0)
    hub.imu.reset_heading(0)
    Fmin = 400
    while hub.imu.ready() == False:
        wait(1000)
    if Angle_target < 0:
        Error = -11
        while Error < -1:
            print(Error)
            motorD.run(Fmin*Error)
            motorE.run(Fmin*Error)
            Error = Angle_target - hub.imu.heading()
    elif Angle_target > 0:
        Error = 20
        while Error > 1:
            motorD.run(Fmin*Error)
            motorE.run(Fmin*Error)
            Error = Angle_target - hub.imu.heading()
    print(Error)

            
while True:
    print(hub.imu.heading())
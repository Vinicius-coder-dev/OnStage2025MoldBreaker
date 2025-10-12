from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, Matrix, vector

hub = PrimeHub(observe_channels=[1])
OwnAdress = 3
Adress = 0
Command = 0
sensE = ColorSensor(Port.B)
sensD = ColorSensor(Port.A)
motorD = Motor(Port.E)
motorE = Motor(Port.F)
#motorUp = Motor(Port.D)
#motorPickup = Motor(Port.C)
PI = 3.1415
X = Matrix([[1,0,0]])
hub.imu.reset_heading(0)
hub.imu.settings(2.0, 2500.0, 360,(0.0, 0.0, 0.0), (367.35, 358.5, 360.38), (9806.65, -9806.65, 9806.65, -9806.65, 9806.65, -9806.65))
def LineFollow():
    BrancoEsq = 255
    PretoEsq = 0
    BrancoDir = 255
    PretoDir = 0
    Fe = 0
    Fd = 0
    Fmin = 400
    kp = 10
    erro = 0
    vneE = sensE.reflection()
    vneD = sensD.reflection()
    if ( vneD > 100):
        vneD = 100
    if ( vneD < 0):
        vneD = 0
    if ( vneE > 100):
        vneE = 100
    if ( vneE < 0):
        vneE = 0
    erro = vneE - vneD

    Fe = Fmin + (kp * erro)
    Fd = Fmin - (kp * erro)
    motorD.run(-Fd)
    motorE.run(Fe)

def TurnAngle(Angle_target):
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


while True:
    data = hub.ble.observe(1)
    if data is not None:
        Adress, Command = data
        print(Adress, Command)
    else:
        Command = 0
        Adress = 0
    if Adress == OwnAdress:
        if Command == 1:# (Teste)virar para a esquerda
            while True:
                LineFollow()
                motorUp.run(-1200)
                if sensE.color() == Color.GREEN:
                    break
            motorD.hold()
            motorE.hold()
            motorD.run(-600)
            motorE.run(-600)
            motorUp.hold()
            wait(1000)
        if Command == 2:# (Teste)virar para direita
            while True:
                LineFollow()
                if sensD.color() == Color.GREEN:
                    break
            motorD.hold()
            motorE.hold()
            motorE.run(600)
            motorD.run(600)
            wait(1000)
        if Command == 3:# Lebre anda até a tartaruga
            while True:
                LineFollow()
                motorUp.dc(90)
                if sensD.color() == Color.RED:
                    break
            motorD.hold()
            motorE.hold()
            motorPickup.hold()
            TurnAngle(10)
            wait(500)
            motorE.run(300)
            motorD.run(-300)
            wait(500)
            motorD.hold()
            motorE.hold()
            while True:
                LineFollow()
                motorUp.dc(90)
                print(sensD.color())
                if sensD.color() == Color.BLUE:
                    wait(100)
                    if sensD.color() == Color.BLUE:
                        break
            motorD.hold()
            motorE.hold()
            motorUp.hold()
        if Command == 4:# Chegar até o Arbusto Raposa
            while True:
                LineFollow()
                motorUp.run(200)
                if sensD.color() == Color.GRAY:
                    break
            motorE.hold()
            motorD.hold()
            motorUp.hold()
            motorPickup.run(200)
            wait(200)
            motorPickup.hold()
            while True:
                LineFollow()
                if sensD.color() == Color.GREEN and sensE.color() == Color.GREEN:
                    break
            motorD.hold()
            motorE.hold()
            motorPickup.run(-200)
            wait(200)
            motorPickup.hold()
            motorE.run(1200)
            motorD.run(1200)
            wait(1000)
            motorD.hold()
            motorE.hold()
            wait(5000)
            while True:
                LineFollow()
                if sensE.color() == Color.YELLOW:
                    break
            motorE.hold()
            motorD.hold()
            motorE.run(600)
            motorD.run(-600)
            wait(500)
            motorE.hold()
            motorD.hold()
            while True:
                LineFollow()
                if sensD.color() == Color.BLUE:
                    break
            motorD.hold()
            motorE.hold()
        if Command == 5:# Tartaruga gira-gira
            while True:
                LineFollow()
                if sensE.color() == Color.BLUE:
                    break
            motorE.hold()
            motorD.hold()
        if Command == 6:# Lebre observa e espera decisão
            while True:
                LineFollow()
                if sensD.color() == Color.BLUE:
                    break
            motorD.hold()
            motorE.hold()
        if Command == 7:# (Teste)Bicho para em azul
            while True:
                LineFollow()
                if sensD.color() == Color.BLUE:
                    break
            motorD.hold()
            motorE.hold()
        if Command == 8:# Lebre vai e pega a pedra
            while True:
                LineFollow()
                motorUp.dc(90)
                if sensD.color() == Color.GREEN:
                    break
            motorD.hold()
            motorE.hold()
            motorPickup.hold()
            TurnAngle(10)
            wait(500)
            motorE.run(300)
            motorD.run(-300)
            wait(500)
            motorD.hold()
            motorE.hold()
            while True:
                LineFollow()
                motorUp.dc(90)
                print(sensD.color())
                if sensD.color() == Color.BLUE:
                    wait(100)
                    if sensD.color() == Color.BLUE:
                        break
            motorD.hold()
            motorE.hold()
            motorUp.hold()
            while True:
                LineFollow()
                hsv = sensE.hsv(True)
                print(hsv)
                if hsv[0] > 195 and hsv[0] < 213 and hsv[1] > 14 and hsv[1] < 19:
                    wait(100)
                    if hsv[0] > 195 and hsv[0] < 213 and hsv[1] > 14 and hsv[1] < 19:
                        break
            motorE.hold()
            motorD.hold()
            TurnAngle(-60)
            motorD.hold()
            motorE.hold()
            motorE.run(-600)
            motorD.run(600)
            wait(1000)
            motorD.hold()
            motorE.hold()
            motorPickup.run(-500)
            wait(650)
            motorPickup.hold()
            wait(10000)
        if Command == 9:# Galo sai e canta
            while True:
                LineFollow()
                if sensD.color() == Color.GREEN:
                    break
            motorD.hold()
            motorE.hold()
            motorE.run_angle(300,400,Stop.HOLD,False)
            motorD.run_angle(300,-400,Stop.HOLD,True)
            TurnAngle(-80)
            motorD.hold()
            motorE.hold()
            while True:
                LineFollow()
                if sensD.color() == Color.BLUE:
                    wait(100)
                    if sensD.color() == Color.BLUE:
                        break
            motorD.hold()
            motorE.hold()
        if Command == 10:# Lebre vai e coloca a pedra e acaba presa
            while True:
                LineFollow()
                if sensD.color() == Color.RED:
                    break
            motorD.hold()
            motorE.hold()
            wait(1000)
            TurnAngle(70)
            motorD.hold()
            motorUp.hold()
            motorE.hold()
            motorE.run(600)
            motorD.run(-600)
            wait(1000)
            motorD.hold()
            motorE.hold()
            while True:
                motorUp.dc(90)
                LineFollow()
                if sensE.color() == Color.GREEN:
                    wait(100)
                    if sensE.color() == Color.GREEN:
                        break
            motorD.hold()
            motorE.hold()
            TurnAngle(-30)
            motorD.hold()
            motorE.hold()
            wait(1000)
            motorE.run(600)
            motorD.run(-600)
            wait(1000)
            motorD.hold()
            motorE.hold()
            while True:
                LineFollow()
                if sensE.color() == Color.YELLOW:
                    break
            wait(21000)
        if Command == 11:# Lebre vai tirar a bateria
            while True:
                LineFollow()
                motorUp.dc(-90)
                if sensD.color() == Color.YELLOW:
                    break
            motorD.hold()
            motorE.hold()
            motorUp.hold()
            motorD.run(-800)
            motorE.run(800)
            wait(1000)
            TurnAngle(10)
            wait(500)
            motorD.hold()
            motorE.hold()
            while True:
                print(sensE.color())
                LineFollow()
                if sensD.color() == Color.GREEN and sensE.color() == Color.GREEN:
                    break
            motorD.hold()
            motorE.hold()
            TurnAngle(180)
            motorUp.hold()
            motorD.hold()
            motorE.hold()
            motorUp.hold()
            #motorPickup.run(-200)
            wait(200)
            #motorPickup.hold()
            while True:
                LineFollow()
                motorUp.dc(-90)
                if sensE.color() == Color.BLUE:
                    break
            motorUp.hold()
            motorD.hold()
            motorE.hold()
            wait(5000)
        if Command == 12:# Galo vai e se une aos animais
            pass
        if Command == 13:# Tartaruga vai e se une aos animais
            pass
        if Command == 14:# Raposa sai de atras do arbusto
            pass


            
#1 é a raposa    
#2 é a lebre      
#3 é o galo
#4 é a tartaruga
#5 é armadilha

 #Cinza - PegarObjeto
 #Vermelho - Gap de Cima
 #Azul - Parar
 #Verde - Combinação de Giro(esquerda,direita,180)
 #Amarelo - Gap de Baixo

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

OwnAdress = 2
Adress = 0
timer = StopWatch
Command = 0
sensE = ColorSensor(Port.B)
sensD = ColorSensor(Port.A)
motorD = Motor(Port.E)
motorE = Motor(Port.F)
motorUp = Motor(Port.D)
motorPickup = Motor(Port.C)

hub = PrimeHub(observe_channels=[1])
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
    Fmin = 200
    while hub.imu.ready() == False:
        wait(1000)
    if Angle_target < 0:
        Error = -11
        while Error < -1:

            motorD.run(Fmin*Error)
            motorE.run(Fmin*Error)
            Error = Angle_target - hub.imu.heading()
    elif Angle_target > 0:
        Error = 20
        while Error > 1:
            print(hub.imu.heading())
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
            TurnAngle(30)
            motorE.run(300)
            motorD.run(-300)
            wait(500)
            motorD.hold()
            motorE.hold()
            while True:
                LineFollow()
                motorUp.dc(90)
                print(sensD.color())
                if sensD.color() == Color.BLUE and sensE.color() == Color.RED:
                    wait(100)
                    if sensD.color() == Color.BLUE and sensE.color() == Color.RED:
                        break
            motorD.hold()
            motorE.hold()
            motorUp.hold()
        if Command == 4:# Chegar até o Arbusto Raposa
            while True:
                LineFollow()
                motorUp.dc(90)
                hsv = sensD.hsv(True)
                print(hsv)
                if sensD.color() == Color.BLUE and sensE.color() == Color.BLUE:
                    wait(100)
                    if sensD.color() == Color.BLUE and sensE.color() == Color.BLUE:
                        break
            motorE.hold()
            motorD.hold()
            motorUp.hold()
            motorPickup.run(200)
            wait(400)
            motorPickup.hold()
            TurnAngle(50)
            motorD.hold()
            motorE.hold()
            motorD.hold()
            motorE.hold()
            motorE.run_angle(300,350,Stop.HOLD,False)
            motorD.run_angle(300,-350,Stop.HOLD,True)
            motorD.hold()
            motorE.hold()
            wait(3000)
            motorPickup.run(-300)
            wait(400)
            motorPickup.hold()
            TurnAngle(-60)
            while True:
                LineFollow()
                if sensD.color() == Color.GREEN and sensE.color() == Color.GREEN:
                    wait(100)
                    if sensD.color() == Color.GREEN and sensE.color() == Color.GREEN:
                        break
            motorD.hold()
            motorE.hold()
            motorPickup.run(150)
            wait(750)
            motorE.run_angle(300,-350,Stop.HOLD,False)
            motorD.run_angle(300,350,Stop.HOLD,True)
            motorPickup.hold()
            motorD.hold()
            motorE.hold()
            TurnAngle(170)
            motorD.hold()
            motorE.hold()
            wait(500)
            motorD.run_angle(300,400,Stop.HOLD,False)
            motorE.run_angle(300,-400,Stop.HOLD,True)
            while True:
                LineFollow()
                if sensE.color() == Color.YELLOW:
                    break
            motorE.hold()
            motorD.hold()
            motorE.run(600)
            motorD.run(-600)
            wait(2000)
            motorE.hold()
            motorD.hold()
            while True:
                LineFollow()
                if sensD.color() == Color.BLUE:
                    wait(100)
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
                motorUp.dc(-90)
                if sensD.color() == Color.GREEN:
                    wait(100)
                    if sensD.color() == Color.GREEN:
                        break
            motorD.hold()
            motorE.hold()
            motorPickup.run(-400)
            wait(300)
            motorPickup.hold()
            TurnAngle(20)
            motorD.hold()
            motorE.hold()
            motorD.run(-800)
            motorE.run(800)
            wait(800)
            motorD.hold()
            motorE.hold()
            while True:
                LineFollow()
                if sensD.color() == Color.RED and sensE.color() == Color.RED:
                    break
            print("AC")
            motorD.hold()
            motorE.hold()
            TurnAngle(-40)
            motorD.hold()
            motorE.hold()
            motorD.run(-200)
            motorE.run(200)
            wait(500)
            motorD.hold()
            motorE.hold()
            motorPickup.run(100)
            wait(1200)
            motorPickup.hold()
            TurnAngle(-140)
            motorD.hold()
            motorE.hold()
            motorD.run(-200)
            motorE.run(200)
            wait(500)
            motorD.hold()
            motorE.hold()
        if Command == 9:# Galo sai e canta
            while True:
                LineFollow()
                if sensD.color() == Color.BLUE:
                    break
            motorD.hold()
            motorE.hold()           
        if Command == 10:# Lebre vai e coloca a pedra e acaba presa
            while True:
                LineFollow()
                motorUp.dc(-90)
                if sensD.color() == Color.RED:
                    break
            motorD.hold()
            motorE.hold()
            TurnAngle(70)
            motorD.hold()
            motorUp.hold()
            motorE.hold()
            motorE.run_angle(300,700,Stop.HOLD,False)
            motorD.run_angle(300,-700,Stop.HOLD,True)
            while True:
                motorUp.dc(-90)
                LineFollow()
                if sensE.color() == Color.GREEN:
                    break
            motorD.hold()
            motorE.hold()
            TurnAngle(-60)
            while True:
                LineFollow()
                if sensD.color() == Color.BLUE and sensE.color() == Color.BLUE:
                    break
            motorD.hold()
            motorE.hold()
            motorPickup.run(-200)
            wait(200)
            motorPickup.hold()
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
            motorD.hold()
            motorE.hold()
            motorPickup.run(-300)
            wait(500)
            motorPickup.hold()
            while True:
                print(sensE.color())
                LineFollow()
                if sensD.color() == Color.GREEN and sensE.color() == Color.GREEN:
                    break
            motorD.hold()
            motorE.hold()
            motorPickup.run(400)
            wait(500)
            TurnAngle(180)
            motorUp.hold()
            motorD.hold()
            motorE.hold()
            motorUp.hold()
            motorPickup.hold()
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


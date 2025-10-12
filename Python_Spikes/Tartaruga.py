from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

OwnAdress = 4
Adress = 0
Command = 0
sensE = ColorSensor(Port.B)
sensD = ColorSensor(Port.A)
motorD = Motor(Port.E)
motorE = Motor(Port.F)
motorUp = Motor(Port.D)
#motorPickup = Motor(Port.D)

hub = PrimeHub(observe_channels=[1])
def LineFollow():
    BrancoEsq = 255
    PretoEsq = 0
    BrancoDir = 255
    PretoDir = 0
    Fe = 0
    Fd = 0
    Fmin = 600
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
            motorE.run(600)
            motorD.run(600)
            while True:
                LineFollow()
                motorUp.dc(90)
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
                if sensE.color() == Color.GRAY:
                    break
            motorE.hold()
            motorD.hold()
            motorUp.hold()
            while True:
                LineFollow()
                if sensD.color() == Color.GREEN:
                    break
            motorD.hold()
            motorE.hold()
            motorD.run(600)
            motorUp.dc(90)
            motorE.run(600)
            wait(100)
            motorD.hold()
            motorUp.hold()
            motorE.hold()
            while True:
                LineFollow()
                if sensE.color() == Color.GRAY:
                    break
            motorE.hold()
            motorD.hold()
            motorPickup.run(-200)
            wait(200)
            motorPickup.hold()
            motorD.run(-1200)
            motorE.run(1200)
            wait(600)
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
                if sensD.color() == Color.RED:
                    break
            motorD.hold()
            motorE.hold()
            motorD.run(600)
            motorUp.dc(90)
            motorE.run(600)
            wait(100)
            motorD.hold()
            motorUp.hold()
            motorE.hold()
            while True:
                motorUp.dc(90)
                LineFollow()
                if sensE.color() == Color.GREEN:
                    break
            motorD.hold()
            motorE.hold()
            motorD.run(-600)
            motorE.run(-600)
            motorUp.hold()
            wait(1000)
            while True:
                LineFollow()
                if sensD.color() == Color.GRAY:
                    break
            motorD.hold()
            motorE.hold()
            motorPickup.run(-200)
            wait(200)
            motorPickup.hold()
        if Command == 11:# Lebre vai tirar a bateria
            while True:
                LineFollow()
                motorUp.dc(90)
                if sensD.color() == Color.YELLOW:
                    break
            motorD.hold()
            motorE.hold()
            motorUp.hold()
            while True:
                motorD.run(-200)
                motorE.run(200)
                if sensD.color() == Color.BLACK:
                    break
            motorD.run(100)
            motorE.run(100)
            wait(200)
            motorD.hold()
            motorE.hold()
            while True:
                LineFollow()
                if sensE.color() == Color.GREEN:
                    break
            motorD.hold()
            motorE.hold()
            motorD.run(-600)
            motorE.run(-600)
            motorUp.hold()
            while True:
                LineFollow()
                motorUp.dc(90)
                if sensD.color() == Color.GRAY:
                    break
            motorD.hold()
            motorE.hold()
            motorUp.hold()
            motorPickup.run(-200)
            wait(200)
            motorPickup.hold()
        


            
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
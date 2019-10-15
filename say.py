from gpiozero import Buzzer
from time import sleep

pinBuzzer = 21

buzzer = Buzzer(pinBuzzer)

def hello():
    print("Hello")
    for i in range (3):
        buzzer.on()
        sleep(0.2)
        buzzer.off()
        sleep(0.2)

def yes():
    print("Yes")
    buzzer.on()
    sleep(0.5)
    buzzer.off()

def no():
    print("No")
    for i in range(3):
        buzzer.on()
        sleep(0.1)
        buzzer.off()
        sleep(0.1)


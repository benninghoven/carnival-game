from screamer import *
import RPi.GPIO as GPIO
from servo import UnmuteMic
import sys

TRIG = 4
ECHO = 17

if len(sys.argv) == 2:
    UnmuteMic()


def SetupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

def Destroy():
    GPIO.cleanup
    print("\n💥 destroyed")
    exit()

def GetDistance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    while GPIO.input(ECHO) == False:
        start = time.time()

    while GPIO.input(ECHO) == True:
        end = time.time()
    sig_time = end-start

    distance = sig_time / 0.000148
    if distance > 1000:
        return -1
    return int(distance)

def StandBack():
    print("Standing User Back")
    minDistance = 10
    maxDistance = 100
    combo = 2
    counter = 0
    tempy = 0
    while True:
        distance = GetDistance()
        print(f"{distance}")
        if distance <= maxDistance and distance >= minDistance:
            counter += 1
            print(f"COMBO {counter}")
        else:
            counter = 0

        if counter >= combo:
            break
        time.sleep(.1)

SetupGPIO()
s = Screamer()
s.StartUp()

while True:
    try:
        name = input("enter name\n")
        if name == "blake":
            break
        StandBack()
        nameScoreDict = s.Play(name)
        print(nameScoreDict["name"])
        print(nameScoreDict["score"])
    except KeyboardInterrupt:
        Destroy()

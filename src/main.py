from screamer import *
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG = 4
ECHO = 18
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def Destroy():
    GPIO.cleanup
    print("destroyed")

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
    return int(distance)

def StandBack():
    print("Standing User Back")
    for i in range(0,10):
        print(GetDistance())
        time.sleep(.1)


s = Screamer()

Destroy()

StandBack()
Destroy()
exit()

while True:
    name = input("enter name\n")
    if name == "blake":
        break
    StandBack()
    s.Play(name)

Destroy()

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 4
ECHO = 18

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

def GetDistance():
    while GPIO.input(ECHO) == False:
        start = time.time()
    while GPIO.input(ECHO) == True:
        end = time.time()
    sig_time = end-start
    return int(sig_time / 0.000148)


GPIO.cleanup()

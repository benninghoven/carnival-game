from adafruit_servokit import ServoKit
import time

kit = ServoKit(channels=8)
servo = kit.servo[1]

SLEEP = .1

def UnmuteMic():
    servo.angle = 0
    time.sleep(SLEEP)
    servo.angle = 10
    time.sleep(SLEEP)
    servo.angle = 0


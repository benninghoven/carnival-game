import numpy as np
import sounddevice as sd
from rpi_ws281x import *
import time
import random
import RPi.GPIO as GPIO


DEBUG = False
COLORS = {
        "red" : Color(255,0,0),
        "orange" : Color(255,165,0),
        "yellow" : Color(255,255,0),
        "green" : Color(0,128,0),
        "blue" : Color(0,0,255),
        "purple" : Color(75,0,130),
        "pink" : Color(238,130,238),
        "death" : Color(0,0,0)
        }

TRIG = 4
ECHO = 17
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

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
    minDistance = 10 # CHANGE ME
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

class Screamer():
    def __init__(self):
        print("screamer screamin")
        # Mic
        self.maxVolume = 277
        self.volumeList = []
        # RGBStrip
        self.LED_COUNT      = 100      # Number of LED pixels.
        self.LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
        self.LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
        self.LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
        self.LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
        if DEBUG:
            self.LED_BRIGHTNESS = 5
        self.LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
        self.LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
        self.AFK = True
        self.strip = Adafruit_NeoPixel(
                                self.LED_COUNT, 
                                self.LED_PIN, 
                                self.LED_FREQ_HZ,
                                self.LED_DMA,
                                self.LED_INVERT,
                                self.LED_BRIGHTNESS,
                                self.LED_CHANNEL
                                )
        self.dict = {}
        for x in range(0, self.LED_COUNT):
            self.dict[x] = True
        self.strip.begin()
    


    def ScoreToPercent(self,score):
        return int((score / self.maxVolume) * 100)
        
    def AudioCallBack(self, inData, frames, time, status):
        volume = int(np.linalg.norm(inData) * 10)
        self.volumeList.append(volume)
        percentageScore = int((volume / self.maxVolume) * 100)
        self.Surge(percentageScore)
        self.Visualize()
        if DEBUG:
            print(f"{volume} {percentageScore}%")


    def Listen(self, duration = 3):
        stream = sd.InputStream(callback=self.AudioCallBack)
        with stream:
            sd.sleep(duration * 1000)
        self.volumeList.sort()
        highestScore = self.volumeList[-1]
        self.volumeList = [] # clear it for the next user
        #return self.ScoreToPercent(highestScore)
        return highestScore 

    def __str__(self):
        return str(self.dict)

    def Visualize(self,color = "red"):
        color = COLORS[color]
        for x in range(0,self.LED_COUNT):
            if self.dict[x]:
                self.strip.setPixelColor(x,color)
            else:
                self.strip.setPixelColor(x,Color(0,0,0))
        self.strip.show() # show is refresh

    def Surge(self,val = 0):
        if val < 0:
            val = 0
        elif val > 100:
            val = 100
        for i in range(0,self.LED_COUNT):
            if i <= val: # in the money
                if not self.dict[i]:
                    self.dict[i] = True
            else:
                if self.dict[i]:
                    self.dict[i] = False

    def SetLightsAllTrue(self):
        for i in range(0,self.LED_COUNT):
            if not self.dict[i]:
                self.dict[i] = True

    def SetLightsAllFalse(self):
        for i in range(0,self.LED_COUNT):
            if self.dict[i]:
                self.dict[i] = False

    def StartUp(self, duration = 3):
        print("STARTING UP")
        self.strip.setBrightness(0);
        t_end = time.time() + duration # 10 seconds
        size = len(COLORS)
        percents = []
        for i in range(0,size):
            percents.append(int((i/size) * 100))
        for i in range(0,self.LED_COUNT):
            if i <= percents[1]:
                self.strip.setPixelColor(i, COLORS["pink"])
            elif i <= percents[2]:
                self.strip.setPixelColor(i, COLORS["purple"])
            elif i <= percents[3]:
                self.strip.setPixelColor(i, COLORS["blue"])
            elif i <= percents[4]:
                self.strip.setPixelColor(i, COLORS["green"])
            elif i <= percents[5]:
                self.strip.setPixelColor(i, COLORS["yellow"])
            elif i <= percents[6]:
                self.strip.setPixelColor(i, COLORS["orange"])
            else:
                self.strip.setPixelColor(i, COLORS["red"])
        for i in range(0,255, 1):
            self.strip.setBrightness(i);
            self.strip.show() # show is refresh
            time.sleep(.005)
            sleep = .1

        self.Visualize("yellow")
        print("ready")

    def TurnLightsOff(self):
        self.SetLightsAllTrue
        for i in range(0,self.LED_COUNT):
            if self.dict[i]:
                self.strip.setPixelColor(i, Color(0,0,0))
        self.strip.show()

    def StartCountDown(self,countDownTime = 1):
        self.SetLightsAllTrue()
        quarters = [25,50,75,100]
        color = "red"
        for i in range(0,4):
            print("BEEP")
            for j in range(0,self.LED_COUNT):
                if j > 75:
                    color = "green"
                else:
                    color = "red"
                if j <= quarters[i]:
                    self.strip.setPixelColor(j, COLORS[color])
                else:
                    self.strip.setPixelColor(j, COLORS["death"])
            self.strip.show()
            time.sleep(countDownTime)




    def Play(self, name = "Kyle"):
        StandBack()
        print(f"{name} started playing")
        self.StartCountDown()
        highScore = self.Listen()
        print(f"highscore: {highScore}")
        self.Surge(self.ScoreToPercent(highScore))
        self.Visualize("green")
        time.sleep(5)
        self.SetLightsAllTrue
        self.Visualize(random.choice(list(COLORS.keys())))
        return {
            "name": name,
            "score": highScore
                }



            

        







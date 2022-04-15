from rpi_ws281x import *
import time

colors = {
        "red" : Color(255,0,0),
        "orange" : Color(255,165,0),
        "yellow" : Color(255,255,0),
        "green" : Color(0,128,0),
        "blue" : Color(0,0,255),
        "purple" : Color(75,0,130),
        "pink" : Color(238,130,238)
        }

class Strip():

    def __init__(self):
        self.debug = True 
        self.LED_COUNT      = 100      # Number of LED pixels.
        self.LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
        self.LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
        self.LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
        self.LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
        if self.debug:
            self.LED_BRIGHTNESS = 5
        self.LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
        self.LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
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

        self.SetRed()


    def __str__(self):
        return str(self.dict)

    def SetRed(self):
        for x in range(0,self.LED_COUNT):
            self.strip.setPixelColor(x,Color(255,0,0))

    def Visualize(self,color = "red"):
        color = colors[color]
        for x in range(0,self.LED_COUNT):
            if self.dict[x]:
                self.strip.setPixelColor(x,color)
            else:
                self.strip.setPixelColor(x,Color(0,0,0))
        self.strip.show() # show is refresh

    def Test(self):
        print("TESTING")
        for x in range(0,100):
            if x > 80:
                self.dict[x] = False
    
    def Surge(self,val):
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

    def AllTrue(self):
        for i in range(0,self.LED_COUNT):
            if not self.dict[i]:
                self.dict[i] = True

    def Rainbow(self, duration):
        self.AllTrue()
        t_end = time.time() + duration # 10 seconds
        size = len(colors)
        percents = []
        for i in range(0,size):
            percents.append(int((i/size) * 100))
        while time.time() < t_end:
            for i in range(0,self.LED_COUNT):
                if i <= percents[1]:
                    self.strip.setPixelColor(i, colors["red"])
                elif i <= percents[2]:
                    self.strip.setPixelColor(i, colors["orange"])
                elif i <= percents[3]:
                    self.strip.setPixelColor(i, colors["yellow"])
                elif i <= percents[4]:
                    self.strip.setPixelColor(i, colors["green"])
                elif i <= percents[5]:
                    self.strip.setPixelColor(i, colors["blue"])
                elif i <= percents[6]:
                    self.strip.setPixelColor(i, colors["purple"])
                else:
                    self.strip.setPixelColor(i, colors["pink"])

            self.strip.show() # show is refresh

    def Barber(self, duration): 
        self.AllTrue()
        for i in range(0,self.LED_COUNT):
            if i % 2:
                self.dict[i] = True
            else:
                self.dict[i] = False 

        t_end = time.time() + duration # 10 seconds
        while time.time() < t_end:
            for i in range(0,self.LED_COUNT):
                self.dict[i] = not self.dict[i]
            time.sleep(0.25)
            self.Visualize(3)
    def Off(self):
        self.AllTrue
        for i in range(0,self.LED_COUNT):
            self.strip.setPixelColor(i, Color(0,0,0))
        self.strip.show() # show is refresh
            

        






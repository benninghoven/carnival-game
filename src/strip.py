from rpi_ws281x import *
import time

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

    def Visualize(self,color = 1):

        if color == 1:
            color = Color(255,0,0)
        elif color == 2:
            color = Color(0,255,0)
        elif color == 3:
            color = Color(0,0,255)
        elif color == 4:
            color = Color(148,143,143)
        else:
            color = Color(255,0,0)

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






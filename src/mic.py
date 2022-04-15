import numpy as np
import sounddevice as sd
import time

class Mic():
    
    def __init__(self):
        self.debug = False 
        self.volume = 0 # Max - 277
        self.volumeList = []
        
    
    def AudioCallBack(self, inData, frames, time, status):
        self.volume = int(np.linalg.norm(inData) * 10)
        self.volumeList.append(self.volume)
        if self.debug:
            print(self.volume)

    def Listen(self, duration = 3):
        stream = sd.InputStream(callback=self.AudioCallBack)
        with stream:
            sd.sleep(duration * 1000)
        self.volumeList.sort()
        highestScore = self.volumeList[-1]
        self.volumeList = [] # clear it for the next user
        return highestScore



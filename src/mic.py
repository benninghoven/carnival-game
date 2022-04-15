import numpy as np
import sounddevice as sd
from strip import Strip 

duration = 600 #in seconds

lst = []

strip = Strip()

def audio_callback(indata, frames, time, status):
    volume_norm = int(np.linalg.norm(indata) * 10) #Max 512/260 if sudo
    dog = int(volume_norm / 260 * 100)
    strip.Surge(dog)
    strip.Visualize("green")
    print(int(volume_norm))

    lst.append(int(volume_norm))

stream = sd.InputStream(callback=audio_callback)
with stream:
   sd.sleep(duration * 1000)

"""
lst.sort()

for x in lst:
    print(x)

dog = input("press x")
"""

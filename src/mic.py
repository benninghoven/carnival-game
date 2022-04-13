#!/usr/bin/env python3
import numpy as np
import sounddevice as sd

duration = 3 #in seconds

lst = []

def audio_callback(indata, frames, time, status):
   volume_norm = int(np.linalg.norm(indata) * 10) # Max is 512
   print(f"{int(volume_norm / 512 * 100)}%")
   lst.append(int(volume_norm))

stream = sd.InputStream(callback=audio_callback)

with stream:
   sd.sleep(duration * 1000)

lst.sort()

for x in lst:
    print(x)

dog = input("press x")

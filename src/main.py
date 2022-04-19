from screamer import *
from servo import UnmuteMic
import sys

if len(sys.argv) == 2:
    UnmuteMic()

s = Screamer()
s.StartUp()
while True:
    try:
        nameScoreDict = s.Play("blake")
        print(nameScoreDict["name"])
        print(nameScoreDict["score"])
    except KeyboardInterrupt:
        s.TurnLightsOff()
        Destroy()


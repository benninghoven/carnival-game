from screamer import *
from servo import UnmuteMic
import sys
from gui import GUI

if len(sys.argv) == 2:
    UnmuteMic()

#s = Screamer()
#s.StartUp()

gui = GUI()

while True:
    try:
        pass
    except KeyboardInterrupt:
        gui.s.TurnLightsOff()
        Destroy()


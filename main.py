from weioLib import weioControl
from weioLib.weio import *

w = weioControl.WeioControl()

def myProc():
    print("hello world")
    
    for a in range(3):
        digitalWrite(18,HIGH)
        print("h")
        delay(1000)

        digitalWrite(18,LOW)
        print("l")
        delay(1000)
    w.stop()

attach.process(myProc)

w.start()

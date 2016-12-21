from weioLib.weio import *

def main():
    print("hello world")
    
    for a in range(3):
        digitalWrite(18,HIGH)
        print("h")
        delay(1000)

        digitalWrite(18,LOW)
        print("l")
        delay(1000)

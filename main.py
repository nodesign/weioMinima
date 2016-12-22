import sys
from weioLib.weio import *

def main(args):
    print("hello world")
    
    for a in range(3):
        digitalWrite(18,HIGH)
        print("h")
        delay(1000)

        digitalWrite(18,LOW)
        print("l")
        delay(1000)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

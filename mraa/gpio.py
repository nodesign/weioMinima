from IoTPy.core.gpio import GPIO
from common import iotpyGpio
from common import WEIO_SERIAL_LINKED

# Gpio Output modes
MODE_STRONG = GPIO.OUTPUT #   /**< Default. Strong High and Low */
MODE_PULLUP = GPIO.PULL_UP #   /**< Resistive High */
MODE_PULLDOWN = GPIO.PULL_DOWN # /**< Resistive Low */
MODE_HIZ = GPIO.INPUT #       /**< High Z State */

# Gpio Direction options
DIR_OUT = GPIO.OUTPUT #      /**< Output. A Mode can also be set */
DIR_IN = GPIO.INPUT #       /**< Input */
DIR_OUT_HIGH = 100 # /**< Output. Init High */
DIR_OUT_LOW = 200 #   /**< Output. Init Low */

# Gpio Edge types for interrupts
EDGE_NONE = GPIO.NONE #   /**< No interrupt on Gpio */
EDGE_BOTH = GPIO.CHANGE #   /**< Interrupt on rising & falling */
EDGE_RISING = GPIO.RISE # /**< Interrupt on rising only */
EDGE_FALLING = GPIO.FALL # /**< Interrupt on falling only */


class Gpio(object):

    def __init__(self, pin, owner=True, raw=False):
        """
        Owner means that fs will destroy object after use, if false it will less it open
        raw means that will give raw pin numbers from kernel

        __init__(mraa::Gpio self, int pin, bool owner=True, bool raw=False) -> Gpio

        Parameters
        ----------
        pin: int
        owner: bool
        raw: bool

        __init__(mraa::Gpio self, int pin, bool owner=True) -> Gpio

        Parameters
        ----------
        pin: int
        owner: bool

        __init__(mraa::Gpio self, int pin) -> Gpio

        Parameters
        ----------
        pin: int

        """
        # cnt = 0
        # while(WEIO_SERIAL_LINKED is False):
        #     cnt+=1
        #     if(cnt>10):
        #         print "LPC is not connected"
        #         exit()

        self.pin = iotpyGpio.GPIO(pin)
        self.direction = None
        self.pinNumber = None
        self.edgeDetection = None

    def edge(self, mode):
        """
        edge(Gpio self, mraa::Edge mode) -> mraa::Result

        Parameters
        ----------
        mode: enum mraa::Edge

        """
        self.edgeDetection = mode

    def isr(self, mode, pyfunc, args):
        """
        isr(Gpio self, mraa::Edge mode, PyObject * pyfunc, PyObject * args) -> mraa::Result

        Parameters
        ----------
        mode: enum mraa::Edge
        pyfunc: PyObject *
        args: PyObject *

        """
        self.pin.attach_irq(mode, callback, args, debounceTime=10)

    def isrExit(self):
        """
        isrExit(Gpio self) -> mraa::Result

        Parameters
        ----------
        self: mraa::Gpio *

        """
        self.pin.detach_irq()

    def mode(self, mode):
        """
        mode(Gpio self, mraa::Mode mode) -> mraa::Result

        Parameters
        ----------
        mode: enum mraa::Mode

        """
        self.direction = mode
        if (mode is GPIO.OUTPUT):
            self.pin.setup(GPIO.OUTPUT)
        else :
            print(GPIO.INPUT, mode)
            self.pin.setup(GPIO.INPUT, mode)


    def dir(self, dir):
        """
        dir(Gpio self, mraa::Dir dir) -> mraa::Result

        Parameters
        ----------
        dir: enum mraa::Dir

        """
        self.direction = dir
        if (dir is GPIO.OUTPUT):
            self.pin.setup(GPIO.OUTPUT)
        else :
            self.mode(dir)

        if (dir==100):
            self.write(1)
        elif (dir==200):
            self.write(0)

    def readDir(self):
        """
        readDir(Gpio self) -> mraa::Dir

        Parameters
        ----------
        self: mraa::Gpio *

        """
        return self.direction
        #return _mraa.Gpio_readDir(self)

    def read(self):
        """
        read(Gpio self) -> int

        Parameters
        ----------
        self: mraa::Gpio *

        """
        self.pin.read()

    def write(self, value):
        """
        write(Gpio self, int value) -> mraa::Result

        Parameters
        ----------
        value: int

        """
        #return _mraa.Gpio_write(self, value)
        self.pin.write(value)

    def useMmap(self, enable):
        """
        useMmap(Gpio self, bool enable) -> mraa::Result

        Parameters
        ----------
        enable: bool

        """
        print("MMAP not available")
        return -1


    def getPin(self, raw=False):
        """
        getPin(Gpio self, bool raw=False) -> int

        Parameters
        ----------
        raw: bool

        getPin(Gpio self) -> int

        Parameters
        ----------
        self: mraa::Gpio *

        """
        return self.pinNumber

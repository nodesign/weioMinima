import platform
from IoTPy.pyuper.weio import WeIO
from IoTPy.pyuper.utils import IoTPy_APIError, errmsg
import signal

# If serial connection is opened for coprocessor
WEIO_SERIAL_LINKED = False
iotpyGpio = None

def adcRawBits():
    """adcRawBits() -> unsigned int
    WeIO has ADC of 10bits precision
    """
    return 10

def adcSupportedBits():
    """adcSupportedBits() -> unsigned int"""
    return 10

def addSubplatform(subplatformtype, uart_dev):
    """
    addSubplatform(mraa::Platform subplatformtype, std::string uart_dev) -> mraa::Result

    Parameters
    ----------
    subplatformtype: enum mraa::Platform
    uart_dev: std::string

    """
    return None

def aioFromDesc(desc):
    """
    aioFromDesc(std::string desc) -> Aio

    Parameters
    ----------
    desc: std::string

    """
    return None

def getDefaultI2cBus(*args):
    """
    getDefaultI2cBus(int platform_offset) -> int

    Parameters
    ----------
    platform_offset: int

    getDefaultI2cBus() -> int
    """
    return None

def getI2cBusCount():
    """getI2cBusCount() -> int"""
    return None

def getI2cBusId(i2c_bus):
    """
    getI2cBusId(int i2c_bus) -> int

    Parameters
    ----------
    i2c_bus: int

    """
    return None

def getPinCount():
    """getPinCount() -> unsigned int"""
    return 32


def getPinName(pin):
    """
    getPinName(int pin) -> std::string

    Parameters
    ----------
    pin: int

    """
    return None

def getPlatformName():
    """getPlatformName() -> std::string"""
    return "weio mraa"

def getPlatformType():
    """mraa::Platform"""
    return platform.uname()

def getPlatformVersion(*args):
    """
    getPlatformVersion(int platform_offset) -> std::string

    Parameters
    ----------
    platform_offset: int

    getPlatformVersion() -> std::string
    """
    return platform

def getSubPlatformId(pin_or_bus_index):
    """
    getSubPlatformId(int pin_or_bus_index) -> int

    Parameters
    ----------
    pin_or_bus_index: int

    """
    return None

def getSubPlatformIndex(pin_or_bus_id):
    """
    getSubPlatformIndex(int pin_or_bus_id) -> int

    Parameters
    ----------
    pin_or_bus_id: int

    """
    return None


def getVersion():
    """
    std::string

    """
    return "1.5.5"

def gpioFromDesc(desc):
    """
    gpioFromDesc(std::string desc) -> Gpio

    Parameters
    ----------
    desc: std::string

    """
    return None

def hasSubPlatform():
    """hasSubPlatform() -> bool"""
    return False

def init():
    global iotpyGpio
    try :
        print("connecting to LPC")
        iotpyGpio = getIotPyObject() # will return iotpy object
        WEIO_SERIAL_LINKED = True
        return True
    except :
        print "LPC not connected"
        return False


def i2cFromDesc(desc):
    """
    i2cFromDesc(std::string desc) -> I2c

    Parameters
    ----------
    desc: std::string

    """
    return None


def isSubPlatformId(pin_or_bus_id):
    """
    isSubPlatformId(int pin_or_bus_id) -> bool

    Parameters
    ----------
    pin_or_bus_id: int

    """
    return False

def pinModeTest(pin, mode):
    """
    pin: int mode: enum mraa::Pinmodes
    result bool
    """
    return None

def printError(result):
    """
    result: enum mraa::Result
    """
    print result

def removeSubplatform(subplatformtype):
    """
    removeSubplatform(mraa::Platform subplatformtype) -> mraa::Result

    Parameters
    ----------
    subplatformtype: enum mraa::Platform

    """
    return None

def setLogLevel(level):
    """
    setLogLevel(int level) -> mraa::Result

    Parameters
    ----------
    level: int

    """
    return None


def initJsonPlatform(path):
    """
    initJsonPlatform(std::string path) -> mraa::Result

    Parameters
    ----------
    path: std::string

    """
    return None


def uartFromDesc(desc):
    """
    uartFromDesc(std::string desc) -> Uart

    Parameters
    ----------
    desc: std::string

    """
    return None

def spiFromDesc(desc):
    """
    spiFromDesc(std::string desc) -> Spi

    Parameters
    ----------
    desc: std::string

    """
    return None


def pwmFromDesc(desc):
    """
    pwmFromDesc(std::string desc) -> Pwm

    Parameters
    ----------
    desc: std::string

    """
    return None

############################################################### WEIO

def stop():
    try :
        print "Stopping and resseting LPC coprocessor"
        iotpyGpio.reset()
        iotpyGpio.ser.close()
    except:
        exit()

signal.signal(signal.SIGTERM, stop)
signal.signal(signal.SIGINT, stop)

def getIotPyObject():
    print "trying to connect"
    numberOfTries = 1000
    cnt = 0
    closed = True

    while closed:
        try:
            u = WeIO()
            print "connected to uper"
            return u
            closed = False
        except IoTPy_APIError, e: # seems can't establish connection with the UPER board
            #details = e.args[0]
            closed = True
            cnt = cnt+1
            if (cnt>numberOfTries):
                closed = False
                print "uper not present"
                return None

# IOTPY GPIO GLOBAL OBJECT

init()

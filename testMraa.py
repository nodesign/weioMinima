import mraa.common
import mraa.gpio as gpio
import time

x = gpio.Gpio(18)
x.dir(gpio.DIR_OUT)

print("blink red led")
for a in range(2):
    x.write(1)
    print(1)
    time.sleep(0.5)
    x.write(0)
    print(0)
    time.sleep(0.5)

y = gpio.Gpio(2)
y.mode(gpio.MODE_PULLUP)
print y.read()

mraa.common.stop()

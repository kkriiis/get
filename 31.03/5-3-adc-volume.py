import RPi.GPIO as gpio
import time

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


def num2dac(value):
    signal = decimal2binary(value)
    gpio.output(dac, signal)
    return signal

def adc():
    value = []
    x = 0
    for i in range(8):
        x = x + 2**(7-i)
        signal = decimal2binary(x)
        gpio.output(dac, signal)
        time.sleep(0.0007)
        comparation = gpio.input(comp)
        if (comparation == 0):
            value.append(0)
            x = x - 2**(7-i)
        else:
            value.append(1)
    voltage = x*3.3/256
    gpio.output(dac, decimal2binary(x))
    gpio.output(leds, 0)
    print("Entered value = {:^3}  -> {}, output voltage = {:.2f}".format(x, value, voltage))
    for i in range (round(8*(x/256))):
        gpio.output(leds[i], 1)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17
leds = [24, 25, 8, 7, 12, 16, 20, 21]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)
gpio.setup(leds, gpio.OUT)

try:
    while True:
        adc()
        
except Exception:
    print("sorry")

finally:
    gpio.output(dac, 0)
    gpio.cleanup(dac)
    gpio.output(leds, 0)
    gpio.cleanup(leds)
import RPi.GPIO as gpio
import time

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

def adc():

    gpio.output(dac, decimal2binary(gpio.input(comp)*256/3.3)) 

def num2dac(value):
    signal = decimal2binary(value)
    gpio.output(dac, signal)
    return signal

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

try:
    while True:
        for i in range(256):
            time.sleep(0.0007)
            signal = num2dac(i)
            voltage = i*3.3/256
            comparation = gpio.input(comp)
            if (comparation == 0):
                print("Entered value = {:^3}  -> {}, output voltage = {:.2f}".format(i, signal, voltage))
                break
except Exception:
    print("sorry")

finally:
    gpio.output(dac, 0)
    gpio.cleanup(dac)
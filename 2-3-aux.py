import RPi.GPIO as gpio
import time

leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]

gpio.setmode(gpio.BCM)
gpio.setup(leds, gpio.OUT)
gpio.setup(aux, gpio.IN)

while 1:
     gpio.output(leds, gpio.input(aux))
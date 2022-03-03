import RPi.GPIO as gpio
import time
import matplotlib as plt 
import matplotlib.pyplot as plt

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0, 0, 0, 0, 0, 0, 0, 0]

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)

gpio.output(dac, number)
time.sleep(1)
gpio.output(dac, 0)
gpio.cleanup()

x = [0, 2, 5, 32, 64, 127, 255]
y = [0.483, 0.483, 0.483, 0.498, 0.823, 1.625, 3.249]
plt.plot(x, y)
plt.show()

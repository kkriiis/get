import matplotlib.pyplot as plt
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
    print("Entered value = {:^3}  -> {}, output voltage = {:.2f}".format(x, value, voltage))
    return x

def work():
    gpio.output(17, 1)
    start_time = time.time()
    data = []
    while adc() < 240:
        data.append(adc())
    
    gpio.output(troyka, 0)
    while adc() > 0:
        data.append(adc())
    
    finish_time = time.time()
    ex_time = finish_time - start_time
    print(ex_time)

    dy = ex_time/len(data)
    y = []
    for i in range(len(data)):
        y.append(start_time + i*dy)

    data_str = [str(item) for item in data]

    with open('data.txt', "w") as f:
        f.write("\n".join(data_str))

    plt.plot(y, data, 'g^')
    plt.show()

dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17

gpio.setmode(gpio.BCM)
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

try:
    work()

except Exception:
    print("Sorry")

finally:
    gpio.output(dac, 0)
    gpio.cleanup(dac)

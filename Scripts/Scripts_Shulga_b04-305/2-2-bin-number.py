
import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
number = []
GPIO.setup(dac, GPIO.OUT)
for i in range (len(dac)):
    number.append(GPIO.input(dac[i]))
for i in range (len(dac)):
    number[i] = random.randint(0, 1)
print(number)

GPIO.output(dac, 0)
for i in range (len(dac)):
    GPIO.output(dac[i], number[i])
time.sleep(15)

GPIO.output(dac, 0)
GPIO.cleanup()
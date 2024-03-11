
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
for i in range (0,100):
    GPIO.output(24, (i%2))
    time.sleep(1)

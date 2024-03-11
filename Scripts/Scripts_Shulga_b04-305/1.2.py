import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
#GPIO.output(24, 1)

while True:
    GPIO.output(24, GPIO.input(25))



# External module imports
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
sensorPin = 20
GPIO.setup(sensorPin, GPIO.IN)

def detected(channel):
    print('I see something')

GPIO.add_event_detect(sensorPin, GPIO.FALLING, callback=detected, bouncetime = 200)

while True:
    print('3.3')
    sleep(0.4)

#!/usr/bin/python
import RPi.GPIO as GPIO
import time
 
def callback(channel):
    if not GPIO.input(channel):
        print("flame detected")
    else:
        print('no flame')

# FLAME SENSOR
FLAME_SENSOR_PIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLAME_SENSOR_PIN, GPIO.IN) 
GPIO.add_event_detect(FLAME_SENSOR_PIN, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(FLAME_SENSOR_PIN, callback)
 
while True:
        time.sleep(0.1)

#!/usr/bin/python
import RPi.GPIO as GPIO
import time

def callback(channel):  
	if not GPIO.input(channel):
		print ("light")
	else:
		print ("no light")

# LIGHT SENSOR
LIGHT_SENSOR_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT_SENSOR_PIN, GPIO.IN)
GPIO.add_event_detect(LIGHT_SENSOR_PIN, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(LIGHT_SENSOR_PIN, callback)

while True:
	time.sleep(0.1)

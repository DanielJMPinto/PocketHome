#!/usr/bin/python
import RPi.GPIO as GPIO
import time

def callback(channel):  
	if not GPIO.input(channel):
		print ("Raining!")
	else:
		print ("Stopped Raining!")

# RAIN SENSOR
RAIN_SENSOR_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(RAIN_SENSOR_PIN, GPIO.IN)
GPIO.add_event_detect(RAIN_SENSOR_PIN, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(RAIN_SENSOR_PIN, callback)

while True:
	time.sleep(0.1)
#!/usr/bin/python
import RPi.GPIO as GPIO
import time

def callback(channel):  
	if GPIO.input(channel):
		print ("Sound!")
	else:
		print ("No sound")

# SOUND SENSOR
SOUND_SENSOR_PIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUND_SENSOR_PIN, GPIO.IN)
GPIO.add_event_detect(SOUND_SENSOR_PIN, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(SOUND_SENSOR_PIN, callback)

while True:
	time.sleep(0.1)

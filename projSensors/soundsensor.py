#!/usr/bin/python
import RPi.GPIO as GPIO
import time

def sound_sensor_callback(channel):  
	if GPIO.input(channel):
		print ("Sound!")

# SOUND SENSOR
SOUND_SENSOR_PIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUND_SENSOR_PIN, GPIO.IN)
GPIO.add_event_detect(SOUND_SENSOR_PIN, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(SOUND_SENSOR_PIN, sound_sensor_callback)

while True:
	time.sleep(0.1)

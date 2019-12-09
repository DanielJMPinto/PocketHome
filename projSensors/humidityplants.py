#!/usr/bin/python
import RPi.GPIO as GPIO
import time 

def callback(channel):  
	if GPIO.input(channel):
		print ("NO MOISTURE")
	else:
		print ("MOISTURE CHECK")

# HUMIDITY PLANTS
HUMIDITYPLANTS_SENSOR_PIN = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(HUMIDITYPLANTS_SENSOR_PIN, GPIO.IN)
GPIO.add_event_detect(HUMIDITYPLANTS_SENSOR_PIN, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(HUMIDITYPLANTS_SENSOR_PIN, callback)

while True:
	time.sleep(0.1)

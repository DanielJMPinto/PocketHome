#!/usr/bin/python
import RPi.GPIO as GPIO
import time 

def humplants_sensor_callback(channel):  
	if not GPIO.input(channel):
		print ("MOISTURE")
	else:
		print ("NO MOISTURE")

# HUMIDITY PLANTS
HUMIDITYPLANTS_SENSOR_PIN = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(HUMIDITYPLANTS_SENSOR_PIN, GPIO.IN)
GPIO.add_event_detect(HUMIDITYPLANTS_SENSOR_PIN, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(HUMIDITYPLANTS_SENSOR_PIN, humplants_sensor_callback)

while True:
	time.sleep(0.1)

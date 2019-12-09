#!/usr/bin/python
import RPi.GPIO as GPIO
import time

def gas_sensor_callback(channel):
	if not GPIO.input(channel):
		print("not gas")
	else:
		print("gas")

# GAS SENSOR
GAS_SENSOR_PIN = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(GAS_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(GAS_SENSOR_PIN, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(GAS_SENSOR_PIN, gas_sensor_callback)
 
while True:
        time.sleep(0.1)

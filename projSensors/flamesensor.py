#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
from datetime import datetime
from sender import Sender
 
def flame_sensor_callback(channel):
	if not GPIO.input(channel):
		print('FLAME')
		val = 1
		msg = {
			'sensorId': 1,
			'sensorType': 'FLAME_SENSOR',
			'value': val,
			'date': str(datetime.now()),
			'houseId': 1,		
		}
		sender.send(msg)

# Configure Sender
sender = Sender()

# FLAME SENSOR
FLAME_SENSOR_PIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLAME_SENSOR_PIN, GPIO.IN) 
GPIO.add_event_detect(FLAME_SENSOR_PIN, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(FLAME_SENSOR_PIN, flame_sensor_callback)
 
while True:
        time.sleep(0.1)


#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
from datetime import datetime
from sender import Sender

def rain_sensor_callback(channel):  
	if not GPIO.input(channel):
		print('RAIN')
		val = 1
	else:
		print('NO_RAIN')
		val = 0
	msg = {
		'sensorId': 6,
		'sensorType': 'RAIN_SENSOR',
		'value': val,
		'date': str(datetime.now()),
		'houseId': 1,
	}
	sender.send(msg)
	time.sleep(3)

# Configure Sender
sender = Sender()

# RAIN SENSOR
RAIN_SENSOR_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(RAIN_SENSOR_PIN, GPIO.IN)
GPIO.add_event_detect(RAIN_SENSOR_PIN, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(RAIN_SENSOR_PIN, rain_sensor_callback)

while True:
	time.sleep(0.1)
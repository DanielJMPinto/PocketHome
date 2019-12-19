#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
from datetime import datetime
from sender import Sender

def gas_sensor_callback(channel):
	if GPIO.input(channel):
		print('GAS')
		val = 1
		msg = {
			'sensorId': 2,
			'sensorType': 'GAS_SENSOR',
			'value': val,
			'date': str(datetime.now()),
			'houseId': 1,
		}
		sender.send(msg)
	time.sleep(3)

# Configure Sender
sender = Sender()

# GAS SENSOR
GAS_SENSOR_PIN = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(GAS_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.add_event_detect(GAS_SENSOR_PIN, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(GAS_SENSOR_PIN, gas_sensor_callback)
 
while True:
        time.sleep(0.1)


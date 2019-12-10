#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
from datetime import datetime
from sender import Sender

def light_sensor_callback(channel):  
	if not GPIO.input(channel):
		print('LIGHT')
		val = 1
	else:
		print('NO_LIGHT')
		val = 0
	msg = {
		'SENSOR_ID': 4,
		'SENSOR': 'LIGHT_SENSOR',
		'VALUE': val,
		'DATE': str(datetime.now()),
	}
	sender.send(msg)

# Configure Sender
if len(sys.argv) != 2:
	print('USAGE: python3 file.py 192.168.X.Y')
	exit()
sender = Sender(sys.argv[1])


# LIGHT SENSOR
LIGHT_SENSOR_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT_SENSOR_PIN, GPIO.IN)
GPIO.add_event_detect(LIGHT_SENSOR_PIN, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(LIGHT_SENSOR_PIN, light_sensor_callback)

while True:
	time.sleep(0.1)

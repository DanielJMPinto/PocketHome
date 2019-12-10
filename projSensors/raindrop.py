#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
from datetime import datetime
from sender import Sender

def rain_sensor_callback(channel):  
	if not GPIO.input(channel):
		print('RAIN')
		val = 'RAIN'
	else:
		print('NO_RAIN')
		val = 'NO_RAIN'
	msg = {
		'SENSOR': 'RAIN_SENSOR',
		'VALUE': val,
		'DATE': str(datetime.now()),
	}
	sender.send(msg)

# Configure Sender
if len(sys.argv) != 2:
	print('USAGE: python3 file.py 192.168.X.Y')
	exit()
sender = Sender(sys.argv[1])

# RAIN SENSOR
RAIN_SENSOR_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(RAIN_SENSOR_PIN, GPIO.IN)
GPIO.add_event_detect(RAIN_SENSOR_PIN, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(RAIN_SENSOR_PIN, rain_sensor_callback)

while True:
	time.sleep(0.1)

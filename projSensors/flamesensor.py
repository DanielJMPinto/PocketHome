#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
from datetime import datetime
from sender import Sender
 
def flame_sensor_callback(channel):
	if not GPIO.input(channel):
		print('FLAME')
		val = 'FLAME'
	else:
		print('NO_FLAME')
		val = 'NO_FLAME'
	msg = {
		'SENSOR': 'FLAME_SENSOR',
		'VALUE': val,
		'DATE': str(datetime.now()),
	}
	sender.send(msg)

# Configure Sender
if len(sys.argv) != 2:
	print('USAGE: python3 file.py 192.168.X.Y')
	exit()
sender = Sender(sys.argv[1])

# FLAME SENSOR
FLAME_SENSOR_PIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLAME_SENSOR_PIN, GPIO.IN) 
GPIO.add_event_detect(FLAME_SENSOR_PIN, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(FLAME_SENSOR_PIN, flame_sensor_callback)
 
while True:
        time.sleep(0.1)


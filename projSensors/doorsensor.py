#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
from datetime import datetime
from sender import Sender

def door_sensor_callback(channel):
	if not GPIO.input(channel):
		print('CLOSED')
		val = 'CLOSED'
	else:
		print('OPEN')
		val = 'OPEN'
	msg = {
		'SENSOR': 'DOOR_SENSOR',
		'VALUE': val,
		'DATE': str(datetime.now()),
	}
	sender.send(msg)

# Configure Sender
if len(sys.argv) != 2:
	print('USAGE: python3 file.py 192.168.X.Y')
	exit()
sender = Sender(sys.argv[1])

# DOOR SENSOR
DOOR_SENSOR_PIN = 26
GPIO.setmode(GPIO.BCM) 
GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP) 
GPIO.add_event_detect(DOOR_SENSOR_PIN, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(DOOR_SENSOR_PIN, door_sensor_callback)

while True:
	time.sleep(1)

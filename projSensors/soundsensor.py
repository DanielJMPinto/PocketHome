#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
from datetime import datetime
from sender import Sender

def sound_sensor_callback(channel):  
	if GPIO.input(channel):
		print('SOUND')
		val = 'SOUND'
		msg = {
			'SENSOR': 'SOUND_SENSOR',
			'VALUE': val,
			'DATE': str(datetime.now()),
		}
		sender.send(msg)

# Configure Sender
if len(sys.argv) != 2:
	print('USAGE: python3 file.py 192.168.X.Y')
	exit()
sender = Sender(sys.argv[1])


# SOUND SENSOR
SOUND_SENSOR_PIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUND_SENSOR_PIN, GPIO.IN)
GPIO.add_event_detect(SOUND_SENSOR_PIN, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(SOUND_SENSOR_PIN, sound_sensor_callback)

while True:
	time.sleep(0.1)
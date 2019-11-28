#!/usr/bin/env python
# https://www.instructables.com/id/Sound-Sensor-Raspberry-Pi/
import RPi.GPIO as GPIO
import time
from datetime import datetime

channel = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
	if GPIO.input(channel):
		print (datetime.now(), " | Sound detected!")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300) # to know when the pin goes HIGH/LOW
GPIO.add_event_callback(channel, callback)

while True:
	time.sleep(1)

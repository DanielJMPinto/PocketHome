#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
from datetime import datetime
from sender import Sender
from picamera import PiCamera


def take_photo():
	# camera = PiCamera()
	# camera.rotation = 180
	# camera.start_preview()
	img_name = 'PIR_image_' + str(datetime.now())
	# camera.capture('./captures/image_%s.jpg' % img_name)
	print("Photo taken! ", img_name)
	# camera.stop_preview()


def motion_sensor_callback(channel):
	if GPIO.input(channel):
		print("MOVEMENT")
		val = 1
		take_photo()
		msg = {
			'sensorId': 5,
			'sensorType': 'PIR_SENSOR',
			'value': val,
			'date': str(datetime.now()),
			'houseId': 1,
		}
		sender.send(msg)
		# Time to stop searching, to not give multiple values
		time.sleep(3)


# Configure Sender
sender = Sender()

# MOTION SENSOR
MOTION_SENSOR_PIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTION_SENSOR_PIN, GPIO.IN)
GPIO.add_event_detect(MOTION_SENSOR_PIN, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(MOTION_SENSOR_PIN, motion_sensor_callback)

while True:
	time.sleep(0.1)
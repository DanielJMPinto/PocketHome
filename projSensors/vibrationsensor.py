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
    img_name = 'KNOCK_image_' + str(datetime.now())
    # camera.capture('./motion_sensor_captures/image_%s.jpg' % img_name)
    print("Photo taken! ", img_name)
    # camera.stop_preview()


def vibration_sensor_callback(channel):
	if GPIO.input(channel):
		print("KNOCK")
        val = 1
		# take_photo()
    	msg = {
				'SENSOR_ID': 10
		    	'SENSOR': 'DOOR_SENSOR',
		    	'VALUE': val,
		    	'DATE': str(datetime.now()),
		    }
		sender.send(msg)
    	# Para multiplos knocks na porta, nao estar sempre a repetir alguem bateu a porta
		time.sleep(3)


# Configure Sender
if len(sys.argv) != 2:
	print('USAGE: python3 file.py 192.168.X.Y')
	exit()
sender = Sender(sys.argv[1])


# VIBRATION SENSOR
VIBRATION_SENSOR_PIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(VIBRATION_SENSOR_PIN, GPIO.IN)
GPIO.add_event_detect(VIBRATION_SENSOR_PIN, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(VIBRATION_SENSOR_PIN, vibration_sensor_callback)

while True:
	time.sleep(0.1)

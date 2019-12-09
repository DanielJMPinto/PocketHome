#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from datetime import datetime
from picamera import PiCamera

def take_photo():
    # camera = PiCamera()
    # camera.rotation = 180
    # camera.start_preview()
    img_name = 'image_' + str(datetime.now())
    # camera.capture('./motion_sensor_captures/image_%s.jpg' % img_name)
    print("Photo taken! ", img_name)
    # camera.stop_preview()

def callback(channel):  
	if GPIO.input(channel):
		print ("movement!")
		take_photo()
	else:
		print ("no movement")

# MOTION SENSOR
MOTION_SENSOR_PIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTION_SENSOR_PIN, GPIO.IN)
GPIO.add_event_detect(MOTION_SENSOR_PIN, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(MOTION_SENSOR_PIN, callback)

while True:
	time.sleep(0.1)
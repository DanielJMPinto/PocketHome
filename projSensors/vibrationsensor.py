#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import datetime
from picamera import PiCamera

# http://www.piddlerintheroot.com/vibration-sensor/

#GPIO SETUP
channel = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

#camera = PiCamera()
#camera.rotation = 180

def take_photo():
#    camera.start_preview()
    img_name = 'image_' + str(datetime.datetime.now())
#    camera.capture('./door_knock_captures/image_%s.jpg' % img_name)
#    camera.stop_preview()
    print("Photo taken! ", img_name)

def callback(channel):
        if GPIO.input(channel):
                print (datetime.datetime.now(), " | Vibration Detected!")
                take_photo()

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
    print("waiting to vibration...")
    time.sleep(1)

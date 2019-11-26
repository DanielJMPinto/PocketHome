import RPi.GPIO as GPIO
import time
from datetime import datetime
from picamera import PiCamera

# https://www.hackster.io/hardikrathod/pir-motion-sensor-with-raspberry-pi-415c04

# https://www.hackster.io/hardikrathod/pir-motion-sensor-with-raspberry-pi-415c04

# https://www.hackster.io/hardikrathod/pir-motion-sensor-with-raspberry-pi-415c04

SENSOR_PIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

camera = PiCamera()
camera.rotation = 180

def take_photo():
    camera.start_preview()
    img_name = 'image_' + str(datetime.now())
    camera.capture('./motion_sensor_captures/image_%s.jpg' % img_name)
    print("Photo taken! ", img_name)
    camera.stop_preview()

try:
    time.sleep(2) # to stabilize sensor
    while True:
        print('watching...')
        if GPIO.input(23):
            print("MOTION DETECTED!")
            take_photo()
            time.sleep(5)
        time.sleep(0.1)


except:
    GPIO.cleanup()

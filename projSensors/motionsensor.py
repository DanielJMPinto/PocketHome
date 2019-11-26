import RPi.GPIO as GPIO
import time

# https://www.hackster.io/hardikrathod/pir-motion-sensor-with-raspberry-pi-415c04

SENSOR_PIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)
i = 0
try:
    time.sleep(2) # to stabilize sensor
    while True:
        if GPIO.input(23):
            print("Motion Detected...")
			print("Photo taken!")
			i = i + 1
    		camera.capture('./projSensors/img/image_%s.jpg' % i)
    		print('A photo has been taken')
			time.sleep(5) #to avoid multiple detection
        time.sleep(0.1) #loop delay, should be less than detection delay

except:
    GPIO.cleanup()

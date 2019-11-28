import RPi.GPIO as GPIO
import time

# Set Broadcom mode so we can address GPIO pins by number.
GPIO.setmode(GPIO.BCM) 

# This is the GPIO pin number we have one of the door sensor
DOOR_SENSOR_PIN = 26

# Set up the door sensor pin.
GPIO.setup(DOOR_SENSOR_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP) 

while True: 
	status = GPIO.input(DOOR_SENSOR_PIN)
	if  not status:
		print("Closed!")
	else:
		print("OPEN!")
	time.sleep(3)


from time import sleep
from datetime import datetime
import RPi.GPIO as GPIO

# RASPY		SENSOR
# 3.3v P1 	VCC (V)
# GND P6	GND (G)
# GNPIO3 P7	SIGNAL (S)
# http://www.uugear.com/portfolio/using-light-sensor-module-with-raspberry-pi/ 
GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

while True:
	value = GPIO.input(4)
	curr_time = datetime.now()
	print(f"{curr_time} Lights on!") if value == 0 else print(f"{curr_time} Lights off!")
	sleep(2.5)

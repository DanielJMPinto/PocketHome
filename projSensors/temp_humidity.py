#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
import dht11
from datetime import datetime
from sender import Sender
# http://www.piddlerintheroot.com/dht11/

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 17
instance = dht11.DHT11(pin=17)

# Configure Sender
sender = Sender()

try:
	while True:
		result = instance.read()
		if result.is_valid():
			print("Temperature: %-3.1f C" % result.temperature)
			# Temperature
			msg = {
				'sensorId': 8,
				'sensorType': 'TEMP_SENSOR',
				'value': result.temperature,
				'date': str(datetime.now()),
				'houseId': 1,
			}
			sender.send(msg)
			print(msg)
			print("Humidity: %-3.1f %%" % result.humidity)
			# Temperature
			msg = {
				'sensorId': 9,
				'sensorType': 'HUM_SENSOR',
				'value': result.humidity,
				'date': str(datetime.now()),
				'houseId': 1,
			}
			print(msg)
			sender.send(msg)
		# enviar valores de temperatura de minuto em minuto
		time.sleep(1)

except KeyboardInterrupt:
	print("Cleanup")
	GPIO.cleanup()

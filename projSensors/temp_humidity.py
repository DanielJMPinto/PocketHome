#!/usr/bin/python

import sys
import Adafruit_DHT
from datetime import datetime

while True:
	hum, temp = Adafruit_DHT.read_retry(11,4)
	print(f"Temp {temp}C | Hum {hum}%")

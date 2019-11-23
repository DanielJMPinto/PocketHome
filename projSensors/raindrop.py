from time import sleep
import datetime
from gpiozero import InputDevice

no_rain = InputDevice(18)
# RAINDROP SENSOR CONNECTED TO GPIO18
# HIGH = No rain | LOW = Rain
print(no_rain)

while True:
	if not no_rain.is_active:
		print(datetime.datetime.now(), "- Started raining!")
	sleep(1)

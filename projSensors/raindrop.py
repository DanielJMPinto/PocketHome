from time import sleep
import datetime
from gpiozero import InputDevice

no_rain = InputDevice(18)
# RAINDROP SENSOR CONNECTED TO GPIO18
# HIGH = No rain | LOW = Rain
# https://raspi.tv/wp-content/uploads/2017/11/Raindrop-sensor-experiment_bb_1000_01.jpg
print(no_rain)

while True:
	if not no_rain.is_active:
		print(datetime.datetime.now(), "- Started raining!")
	sleep(1)

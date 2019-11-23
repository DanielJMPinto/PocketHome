import RPi.GPIO as GPIO
import time

SENSOR_PIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)


def mycallback(channel):
	print("MOVEMENT!!!!")
	# adicionar oq quisermos aqui
	# pex. tirar uma foto c a camara

try:
	GPIO.add_event_detect(SENSOR_PIN, GPIO.RISING, callback=mycallback)
	while True:
		time.sleep(100)
		print("\tWatching......")

except KeyboardInterrupt:
	print("FINISHED!")

GPIO.cleanup()

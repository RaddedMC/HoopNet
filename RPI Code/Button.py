import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
	input_state = GPIO.input(10)
	if input_state == GPIO.HIGH:
		print("Button Pressed")
		time.sleep(0.2)

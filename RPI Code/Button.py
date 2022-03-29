# ES1050 T24HoopNet
# Button.py
# Programmed by JarrettB

import RPi.GPIO as GPIO
import time
import multiprocessing

class Button:

	__button_pin__ = -1

	def __init__(self, pin):
		""" Initialize the button object.
            Takes a pin number in
        """

		# Set up pin
		GPIO.setmode(GPIO.BOARD)
		self.__button_pin__ = pin
		self.GPIO.setup(self.__button_pin__, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # setup(pin, input pin, set initial value to be pulled low (off))

		# Allow the Pi to start checking if the button has been pressed down
		self.__run_proc_from_method_(self.check_for_pressed)

	def check_for_pressed(self):
		""" Check if the button on the pin was pressed down.
			Repeats looking for any changes
		"""
		while True:
			input_state = GPIO.input(self.__button_pin__) # Get the state of the GPIO pin for the button
			if input_state == GPIO.HIGH: # The GPIO pin was made high and the button was pressed
				print("Button Pressed")
				time.sleep(0.2) # Allow time for the button to reset if released

	def __run_proc_from_method_(self, method, data):
		"""Don't use this! This is used to handle multiprocessing."""

		## Check if there is something else happening. To make sure we don't have overlapping instructions, we want only one flash operation running at a time.
		if self.__proc__ != None and self.__proc__.is_alive():
			self.__proc__.kill()

		self.__proc__ = multiprocessing.Process(target=method, args=data)
		self.__proc__.start()

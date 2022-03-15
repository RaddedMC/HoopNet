# ES1050 T24HoopNet
# DoorMotor.py
# Programmed by JamesN / Radded and JarrettB
# Co-designed with JarrettB

import multiprocessing
import time
import RPi.GPIO as GPIO # Requires to do: sudo apt-get install rpi.gpio

class DoorMotor:
    """Represents a URL hoop house lift motor.
    Asynchronously controls the hoop house motor.
    Don't use __lift__, __lower__, or __run_proc_from_method__!
    This object uses a separate process to work asynchronously.
    Changing state while the door is moving will cause the door to stop momentarily and a warning to be logged.

    Use get_moving() to check if the door is moving, if you wish to wait for the door to stop moving before you ask it to do something else.
    """
    # TODO: Fill object with code so that it can actually control the lift door!

    # OOP states
    is_lifted = False
    __proc__ = None

    # CONSTANTS
    duty_cycle = 100 # 0 - 100 (No (low) to high speed)
    motor_lift_lower_time = 5 # seconds

    # Pin things
    __pwm_enable__ = None
    __pins__ = []

    # pins = [enable, input1, input2]
    def __init__(self, pins):
        """Initialize the door motor object.
        """

        # Setup pins
        GPIO.setmode(GPIO.BOARD)
        self.__pins__ = pins
        for pin in pins:
            GPIO.setup(pin, GPIO.out)
        self.__pwm_enable__ = GPIO.PWM(pins[0], 1) # PWN(Pin, Frequency (default 1))

        # Lower door on creation to ensure stored state matches actual state
        self.__run_proc_from_method_(self.__lower__)
        pass


    ### USER-ACCESSIBLE

    def set_state(self, state):
        """Asynchronously lifts or lowers the side door. Use this method to control the doors!
        """

        # If user wants to lift and it isn't lifted already,
        if state and not self.is_lifted: 
            self.__run_proc_from_method_(self.__lift__)

        # If user wants to lower and it isn't lowered already,
        elif not state and self.is_lifted: 
            self.__run_proc_from_method_(self.__lower__)
        
        self.is_lifted = state

    def get_state(self):
        return self.is_lifted

    def get_moving(self):
        return self.__proc__.is_alive()


    ### USER-INACCESSIBLES ###
        
    def __run_proc_from_method_(self, method):
        """Don't use this! This is used to handle multiprocessing. Use the is_moving field to check if the door is moving."""

        ## Check if there is something else happening. To make sure we don't have overlapping instructions, we want only one lift/lower operation running at a time.
        if self.__proc__ != None and self.__proc__.is_alive():
            self.__proc__.kill()
            print("You tried to change the state of the door while it is moving. Try not to do that in the future!") # TODO: Convert to real warning

        self.__proc__ = multiprocessing.Process(target=method)
        self.__proc__.start()

    def __lift__(self):
        """Don't use this! It is just a helper method for DoorMotor.set_state()"""
        print("Started lifting a lift door!")
        # Forward direction for Motor A


        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.HIGH)
        en_pin_A.start(dutyCycle)
        # Forward direction for Motor B
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.HIGH)
        en_pin_B.start(dutyCycle)
        self.__stop_motors__()
        print("Door lifted. Remember that this needs to be actual code at some point!")

    def __lower__(self):
        """Don't use this! It is just a helper method for DoorMotor.set_state()"""
        print("Started lowering a lift door!")

        # Reverse direction for Motor A
        GPIO.output(in1, GPIO.HIGH)
        GPIO.output(in2, GPIO.LOW)
        en_pin_A.start(dutyCycle)
        
        self.__stop_motors__()
        print("Door lowered. Remember that this needs to be actual code at some point!")

    def __stop_motors__(self):
        # The time it takes for the motor to stop
        time.sleep(motor_lift_lower_time)
         # Stop Motor A
        GPIO.output(in1, GPIO.LOW)
        GPIO.output(in2, GPIO.LOW)
        en_pin_A.stop
        # Stop Motor B
        GPIO.output(in3, GPIO.LOW)
        GPIO.output(in4, GPIO.LOW)
        en_pin_B.stop()
# ES1050 T24HoopNet
# SwitchController.py
# Programmed by JamesN / Radded
# Co-designed with JarrettB

# TODO: Config files for this data
motor_pins = [[1, 2, 3], [4, 5, 6]] # sample!
plug_ips = ["192.168.1.140"] # works on James' AP

from KasaSwitch import KasaSwitch
from DoorMotor import DoorMotor
from KasaSwitch import KasaSwitch

import RPi.GPIO as GPIO # Requires to do: sudo apt-get install rpi.gpio

class SwitchController:

    __switches__ = []

    def __init__(self, motor_pins, plug_ips):
        """ Central class to control all plugs and motors.
        Needs a nested arrray of motor pins as such:
        [
            [enable, pin1, pin2], # for each motor
            [enable, pin1, pin2]
        ]

        Needs an array of Kasa IP addresses as such:
        ["192.168.1.140", "192.168.1.128"]
            TODO: add get states!
        """

        GPIO.cleanup() 

        # Add motors
        for motor_pinset in motor_pins:
            self.__switches__.append(DoorMotor(motor_pinset))

        # Add plugs
        for plug_ip in plug_ips:
            self.__switches__.append(KasaSwitch(plug_ip))

    def set_state(self, state):
        for switch in self.__switches__:
            switch.set_state(state)
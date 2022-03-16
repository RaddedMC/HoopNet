# ES1050 T24HoopNet
# SensorController.py
# Programmed by JamesN / Radded
# Co-designed with JarrettB

from Sensor import Sensor

class SensorController:
    
    __sensors__ = []

    def __init__(self, sensor_pins):
        """ Central class to read data from all sensors.
            Needs an array of numbers as sensor pins:
            [1, 2, 3, 4]
        """
        for sensor_pin in sensor_pins:
            self.__sensors__.append(Sensor(sensor_pin))

    def read_all(self):
        """ Reads data from all sensors!
            Returns in the form of a nested array:

            [
                [Humidity, Temperature],   # Sensor 1
                [Humidity, Temperature],   # Sensor 2
                [Humidity, Temperature]    # Sensor 3
            ]

            Humidity readings are a percentage -- communicated as a floating-point value from 0 to 100.

            Temperature readings are degrees Celcius.
        """
        data = []
        for sensor in self.__sensors__:
            data.append(sensor.get_sensor_data())
        
        return data
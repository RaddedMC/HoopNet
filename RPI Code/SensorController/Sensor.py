# ES1050 T24HoopNet
# Sensor.py
# Programmed by JamesN / Radded and JarrettB
# Co-designed with JarrettB

# Install instructions for sensor library at https://mic.st/blog/connect-temperature-and-humidity-sensor-am2320-dht11-or-dht22-to-raspberry-pi/

import Adafruit_DHT

class Sensor:
    """Represents an AM2302 sensor attached to the Pi.
    TODO: make asynchronous!
    """

    sensor_pin = -1
    sensor = None

    def __init__(self, pin, sensor_type = Adafruit_DHT.AM2302):
        self.sensor_pin = pin
        self.sensor = sensor_type

    def get_sensor_data(self):
        """Returns humidity, temperature"""
        return Adafruit_DHT.read_retry(self.sensor, self.sensor_pin)
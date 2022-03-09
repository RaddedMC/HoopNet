# ES1050 T24HoopNet
# Sensor.py
# Programmed by JamesN / Radded
# Co-designed with JarrettB

# Install instructions for sensor library at https://mic.st/blog/connect-temperature-and-humidity-sensor-am2320-dht11-or-dht22-to-raspberry-pi/

class Sensor:
    """Represents an AM2302 sensor attached to the Pi.

    TODO: make asynchronous!
    """

    sensor_pin = -1
    sensor = Adafruit_DHT.AM2302

    def __init__(self, pin, sensor_type = Adafruit):
        self.sensor_pin = pin
        self.sensor = sensor_type
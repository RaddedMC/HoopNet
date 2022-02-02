#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2014 Adafruit Industries
# Orignal Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Modified by: Jarrett Boersen
# Started: Feb 1st, 2022
# Very rudimentary script to control two temperature/humidity sensors using a Rasberry Pi. I added a loop,
# the second sensor, and a few formating tweaks.
# The library is from https://mic.st/blog/connect-temperature-and-humidity-sensor-am2320-dht11-or-dht22-to-raspberry-pi/. 
# The modified script: https://github.com/adafruit/Adafruit_Python_DHT/blob/master/examples/AdafruitDHT.py. 

import sys
import time

import Adafruit_DHT


# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }

# Set the pin numbers for the Pi
pin_sensor_one = 8
pin_sensor_two = 11

# Set the sensor type
sensor = sensor_args['22']

while (True):
    # Try to grab a sensor reading.  Use the read_retry method which will retry up
    # to 15 times to get a sensor reading (waiting 2 seconds between each retry).
    humidity_sensor_one, temperature_sensor_one = Adafruit_DHT.read_retry(sensor, pin_sensor_one)
    humidity_sensor_two, temperature_sensor_two = Adafruit_DHT.read_retry(sensor, pin_sensor_two)

    # Un-comment the line below to convert the temperature to Fahrenheit.
    # temperature = temperature * 9/5.0 + 32

    # Note that sometimes you won't get a reading and
    # the results will be null (because Linux can't
    # guarantee the timing of calls to read the sensor).
    # If this happens try again!
    if humidity_sensor_one is not None and temperature_sensor_one is not None:
        print('Sensor 1: Temp={0:0.1f}ºC Humidity={1:0.1f}%'.format(temperature_sensor_one,  humidity_sensor_one))
    else:
        print('Failed to get reading. Try again!')
        # sys.exit(1)

    if humidity_sensor_two is not None and temperature_sensor_two is not None:
        print('Sensor 2: Temp={0:0.1f)ºC Humidity={1:0.1f}%'.format(temperature_sensor_two, humidity_sensor_two))
    else:
        print('Failed to get reading. Try again!')
        # sys.exit(1)
    time.sleep(1)
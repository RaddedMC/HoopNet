# ES1050 T24HoopNet
# main.py
# Programmed by JamesN / Radded
# Co-designed with JarrettB

# IMPORTS
from SensorController.SensorController import SensorController
from SwitchController.SwitchController import SwitchController
import signal

# THRESHOLD constants, could be useful later
class thresholds:
    THRESHOLD_TEMP = "TEMP"
    THRESHOLD_HUMIDITY = "HUMI"

# THRESHOLDS, to be moved to a file later
threshold = 10 # number
threshold_type = thresholds.THRESHOLD_TEMP

# OUTPUTS, to be moved to a file later
sensor_pins = [1, 2, 3, 4] # TODO: make these a config file
motor_pins = [[5, 6, 7], [8, 9, 10]]
plug_ips = ["192.168.1.142", "192.168.1.100"]

# GLOBALS for I/O
sensor_controller = None
switch_controller = None


# MAIN LOOP
def main():
    while True:
        # Read sensor
        sensor_data = sensor_controller.
        # Check thresholds
        # If out of threshold, open door!
        # Sleep

# SETUP
def setup():
    """ Ran when the daemon starts for the first time -- creates objects and resets everything
    """
    sensor_controller = SensorController(sensor_pins)
    switch_controller = SwitchController(motor_pins, plug_ips)


# SIGNAL HANDLERS
def handle_signal_stop_high():
    pass

def handle_signal_stop_low():
    pass

def handle_signal_return():
    pass

# PRIMARY SIGNAL HANDLER
def signal_handler(sig, frame):
    if sig == signal.SIGUSR1:
        handle_signal_stop_low()

    if sig == signal.SIGUSR2:
        handle_signal_stop_high()

    if sig == signal.SIGCONT:
        handle_signal_return()

if __name__ == main():
    setup()
    main()
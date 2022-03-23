# ES1050 T24HoopNet
# main.py
# Programmed by JamesN / Radded
# Co-designed with JarrettB

# IMPORTS
import sys

# lol import errors
sys.path.append('SensorController')
sys.path.append('SwitchController')
from SensorController import SensorController
from SwitchController import SwitchController
import signal, time

# THRESHOLD constants, could be useful later
class thresholds:
    THRESHOLD_TEMP = 1
    THRESHOLD_HUMIDITY = 0

# THRESHOLDS, to be moved to a file later
threshold = 30 # number
threshold_type = thresholds.THRESHOLD_HUMIDITY

# OUTPUTS, to be moved to a file later
sensor_pins = [17, 27, 22, 10] # TODO: make these a config file
# 'GPIO' numbers in pinout.xyz

motor_pins = [[33, 31, 29], [32, 36, 38]] ### PINOUTS MATCH Yassine's PCB ###
# Hardware numbers in pinout.xyz

plug_ips = ["172.20.10.7"] # Matches James' kasa plug paired to phone

# GLOBALS for I/O
sensor_controller = None
switch_controller = None

# OTHER important globals
door_lifted = False
wait_time = 5 # Seconds
break_loop = False

# MAIN LOOP
def main():
    while not break_loop:
        
        print("AUTO MODE")

        # Read sensor
        sensor_average = sensor_controller.read_average()
        print("Current Humidity: " + str(sensor_average[0] + "%, " + "Current temperature: " + str(sensor_average[1])))
        
        # Check thresholds

        # threshold_test( 
        #   Average temperature or humidity. thresholds.THRESHOLD_HUMIDITY cooresponds to zero, the index of the average humidity value and vice-versa for thresholds.THRESHOLD_TEMPERATURE,
        #   Threshold: pre-defined by user
        #   Larger: This will be false if the doors are lifted, as when the doors are lifted the value must be above threshold.
        # )

        if threshold_test(sensor_average[threshold_type], threshold, not door_lifted):
            print("Conditions failed threshold test!")

            # Change state of door
            door_lifted = not door_lifted

            if (door_lifted): 
                print("Opening doors!")
            else: 
                print("Lowering doors!")
            
            switch_controller.set_state(door_lifted)
        
        time.sleep(wait_time) # Sleep to give the doors time to move and the readings time to settle

# THRESHOLD TEST
def threshold_test(value_to_check, threshold, larger):
    if larger:
        return value_to_check >= threshold
    else:
        return value_to_check <= threshold

# SETUP
def setup():
    """ Ran when the daemon starts for the first time -- creates objects and resets everything
    """
    global sensor_controller
    sensor_controller = SensorController(sensor_pins)

    global switch_controller
    switch_controller = SwitchController(motor_pins, plug_ips)

# SPLASH SCREEN
def splash_screen():
    print("""
         __  __                  _   __     __ 
        / / / /___  ____  ____  / | / /__  / /_          Western University ES1050 W22 T24Hoop
       / /_/ / __ \/ __ \/ __ \/  |/ / _ \/ __/          Jarrett, Yassine, James, Damian, Ethan, Atrin
      / __  / /_/ / /_/ / /_/ / /|  /  __/ /_            
     /_/ /_/\____/\____/ .___/_/ |_/\___/\__/            Developed for Urban Roots London
                      /_/                                HoopNet daemon for Pi
    """)
    import time
    time.sleep(0.33)

# SIGNAL HANDLERS
def handle_signal_stop_high():
    global switch_controller
    switch_controller.set_state(True)

def handle_signal_stop_low():
    global switch_controller
    switch_controller.set_state(False)

def handle_signal_return():
    main() #TODO: this might create a stack overflow over time ,, we should test

# PRIMARY SIGNAL HANDLER
def signal_handler(sig, frame):

    global break_loop
    break_loop = True

    if sig == signal.SIGUSR1:
        handle_signal_stop_low()

    if sig == signal.SIGUSR2:
        handle_signal_stop_high()

    if sig == signal.SIGCONT:
        handle_signal_return()

    break_loop = False


# RUN AT STARTUP!
splash_screen()

# Register signals -- main() will temporarily stop when one of these signals is recieved.
for signaltype in [signal.SIGUSR1, signal.SIGUSR2, signal.SIGCONT]:
    signal.signal(signaltype, signal_handler)

print("Setting up...")
setup()
print("Setup complete!")
main()
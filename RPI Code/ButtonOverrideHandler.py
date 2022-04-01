# ES1050 T24HoopNet
# Overridder.py
# Programmed by JamesN / Radded

# Imports
from gpiozero import Button
import os
from signal import pause

# Helper class
class States:
    auto = 0
    override_closed = 1
    override_open = 2

# Globals
state = States.auto
pin = 4 ## GPIO PIN not hardware pin

# Happens whenever the Pi Button is pressed
def on_press():
    global state
    print("Button pressed!")

    # If the state is 2, this will revert back
    if state == States.override_open:
        state = 0
    else:
        state+=1

    if state == States.auto:
        print("Set to AUTO")
        os.system("python3 Overrider.py auto")
    elif state == States.override_closed:
        # DO OTHER THING
        print("Set to CLOSE")
        os.system("python3 Overrider.py close")
    else:
        # DO FINAL THING
        print("Set to OPEN")
        os.system("python3 Overrider.py open")

# Makes sure command is ran in right place
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Set up pin profile
button = Button(pin)
button.when_pressed = on_press
pause()

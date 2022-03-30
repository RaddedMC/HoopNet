# ES1050 T24HoopNet
# Overridder.py
# Programmed by JamesN / Radded

# Imports
from gpiozero import button
import os

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

    # If the state is 2, this will revert back
    if state == States.override_open:
        state = 0
    else:
        state+=1

    if state == States.auto:
        os.system("python Overrider.py auto")
    elif state == States.override_closed:
        # DO OTHER THING
        os.system("python Overrider.py close")
    else:
        # DO FINAL THING
        os.system("python Overrider.py open")

# Makes sure command is ran in right place
os.chdir(os.path.dirname(os.path.realpath(__file__)))
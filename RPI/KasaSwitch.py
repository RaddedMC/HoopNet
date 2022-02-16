# ES1050 T24HoopNet
# KasaSwitch.py
# Programmed by JamesN / Radded
# Co-designed with JarrettB

# DEPENDENCIES: pip install python-kasa

import asyncio
from kasa import Discover

# This class is designed to be swapped out with other device controllers should URL switch to a different brand of plugs.
class KasaSwitch:
    ip_addr = None
    plug = None

    def __init__(self, ip_addr):
        self.ip_addr = ip_addr
        
        # Connects to the plug early-on to verify if the IP given is correct
        self.plug = asyncio.run(Discover.discover_single(ip_addr))

    def set_state(self, state):
        if (state):
            self.plug.turn_on()
        else:
            self.plug.turn_off()
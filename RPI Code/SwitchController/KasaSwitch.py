# ES1050 T24HoopNet
# KasaSwitch.py
# Programmed by JamesN / Radded
# Co-designed with JarrettB

# DEPENDENCIES: pip install python-kasa

import asyncio
from tempfile import TemporaryFile
from kasa import Discover
import kasa

class KasaSwitch:
    """Represents a TP-Link Smart Plug.

    Runs synchronously, but generates event loop errors that need to be figured out
    Depends on 'python-kasa' from pip
    Will error if the plug isn't found, this will need to be caught by the SwitchController
    """

    ip_addr = None
    plug = None
    __exists__ = True

    def __init__(self, ip_addr):
        """Initialize the plug object and connects to the smart plug at ip_addr_ on your network.
        Will throw an exception if the plug can't be found!
        """
        self.ip_addr = ip_addr
        
        # Connects to the plug early-on to verify if the IP given is correct
        # This will error if the plug isn't available!
        try:
            self.plug = asyncio.run(Discover.discover_single(self.ip_addr))
        except kasa.exceptions.SmartDeviceException:
            print("Unable to connect to the plug at " + ip_addr + ", continuing...")
            self.__exists__ = False

        

    def set_state(self, state):
        """Asynchronously turns your plug either on (state = True) or off (state = False).
        """
        if self.__exists__ == False:
            try:
                self.plug = asyncio.run(Discover.discover_single(self.ip_addr))
                self.__exists__ = True
            except:
                pass
        else:
            if (state):
                asyncio.new_event_loop().run_until_complete(self.plug.turn_on())
            else:
                asyncio.new_event_loop().run_until_complete(self.plug.turn_off())
            asyncio.new_event_loop().run_until_complete(self.plug.update())

    def get_state(self) -> bool:
        """Gets the state of the plug -- is it on or off?
        """
        if self.__exists__ == False:
            try:
                self.plug = asyncio.run(Discover.discover_single(self.ip_addr))
                self.__exists__ = True
            except:
                pass
        else:
            return self.plug.is_on
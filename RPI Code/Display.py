from RPLCD import i2c
from time import sleep
import multiprocessing

class Display:

    """ A class to print to our display module. Can also flash the backlight asyncronously!
    """

    lcdmode = 'i2c'
    cols = 20
    rows = 2
    charmap = 'A00'
    i2c_expander = "PCF8574"
    address = 0x27
    port = 1
    lcd = None
    warned = False
    backlight_state = True
    
    def __init__(self):
        self.lcd = i2c.CharLCD(self.i2c_expander, self.address, self.port, self.charmap, self.cols, self.rows)
        self.lcd.backlight_enabled = self.backlight_state

    def __overflow_warn__(self):
        self.warned = True
        print("Warning: You attempted to print more than " + str(self.cols) + " on one line. This extra text is cut off, ")

    def display(self, string):
        charcount = 0
        for character in string:
            if character == "\n":
                self.lcd.crlf()
                charcount = 0
            charcount += 1
            if (charcount < self.cols):
                self.lcd.write_string(character)
            else:
                self.__overflow_warn__()
        self.warned = False

    def set_backlight_state(self, state):
        self.backlight_state = state
        self.lcd.backlight_enabled = state

    def __flash_backlight_async(self, data):
        for i in range(0,data[1]*2):
            self.backlight_state = not self.backlight_state
            self.lcd.backlight_enabled = not self.lcd.backlight_enabled
            sleep(data[0])

    def flash_backlight(self, delay, flashes):
        self.__run_proc_from_method_(self.__flash_backlight_async, [delay, flashes])

    def __run_proc_from_method_(self, method, data):
        """Don't use this! This is used to handle multiprocessing."""

        ## Check if there is something else happening. To make sure we don't have overlapping instructions, we want only one flash operation running at a time.
        if self.__proc__ != None and self.__proc__.is_alive():
            self.__proc__.kill()

        self.__proc__ = multiprocessing.Process(target=method, args=data)
        self.__proc__.start()

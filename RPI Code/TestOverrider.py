# Run me in a second command line window

import signal, time

print("Started")

# The method to handle any signals
def handler(signum, frame):
    print('Signal handler called with signal', signum)	

# Set up the singals to wait for
signal.signal(signal.SIGUSR1, handler)
signal.signal(signal.SIGCONT, handler)

time.sleep(100)

print("Ended")
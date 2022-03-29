# ES1050 T24HoopNet
# Overridder.py
# Programmed by JarrettB
# Co-designed with JamesN / Radded

import signal, os, argparse, time, subprocess

# The name of the python script to send signals to
script_name = "main.py"

"""This script is used to send override comannds using the command line
Used to send override commands.
Enter a state - Enter either 'open' to raise the side, 'close' to lower the side, 'auto' to resume automatic control.
Optional enter a time - Enter an integer for how long in seconds to override. Only used with 'open' and 'close'.
"""

def main():
	# Set up the command line arguments
	parser = argparse.ArgumentParser(description="Used to send override commands.")
	parser.add_argument("state", help="An String for the door's state. Enter 'open' to raise the side, 'close' to lower the side, 'auto' to resume automatic control.)")
	parser.add_argument("-time", help="An integer for how long in seconds to override. Only used with 'open' and 'close'.") # TODO: Allow other time lengths ex: minutes?

	# Get the values from the command line args
	args = parser.parse_args()
	state = args.state
	if args.time is None:
		wait_time = 0
	else:
		wait_time = int(args.time)

	# Attempt to find the PID for the python script given
	try:
		pid_b = subprocess.check_output(['pgrep -f ' + script_name], shell=True)
		pid_str = ''.join(map(chr, pid_b))
		pid = int(pid_str.split("\n")[0])
	except:
		raise Exception("PID for " + script_name + " cannot be found.")


	if state == "auto" or state == "Auto": # Set to auto state (continue normal functions)
		os.kill(pid, signal.SIGCONT)
	elif state == "close" or state == "Close": # Set to close state (override and send the singal to close)
		os.kill(pid, signal.SIGUSR1) # Send the close signal
		if wait_time > 0: # Check to make sure there's a value for wait_time
			time.sleep(wait_time) # Wait then resume auto state
			os.kill(pid, signal.SIGCONT)
	elif state == "open" or state == "Open": # Set to open state (override and send the singal to open)
		os.kill(pid, signal.SIGUSR2) # Send the open signal
		if wait_time > 0: # Check to make sure there's a value for wait_time
			time.sleep(wait_time) # Wait then resume auto state
			os.kill(pid, signal.SIGCONT)
	else:
		raise NameError("Error invalid input")

if __name__ == "__main__":
	main()
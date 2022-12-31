
#!/bin/bash

cd "/home/pi/HoopNet/RPI Code/"

screen -dmS "hoopnet" python3 main.py &
screen -dmS "hoopnet-button" python3 ButtonOverrideHandler.py &

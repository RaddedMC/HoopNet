from multiprocessing.connection import wait
# IMPORTS
from SwitchController.KasaSwitch import KasaSwitch
from SwitchController.DoorMotor import DoorMotor

def main(): 
    # ---- PLUGS -----
    # ip = "192.168.1.140"
    # print("Getting plug at " + ip)

    # # Connect to plug
    # plug = KasaSwitch(ip)

    # # Turn plug off
    # print("Turning plug off...")
    # plug.set_state(False)
    # print("Plug is " + str(plug.get_state()))

    # import time
    # time.sleep(1)

    # # Turn plug on
    # print("Turning plug on...")
    # plug.set_state(True)
    # print("Plug is " + str(plug.get_state()))


    # ---- LIFT DOOR ----

    import time
    door = DoorMotor()

    while door.get_moving:
        print("Main is waiting for the door to stop lowering lolol")
        time.sleep(1)

if __name__ == "__main__":
    main()
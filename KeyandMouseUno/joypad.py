from pyfirmata import Arduino
from pyfirmata.util import Iterator
import time

# Setup
try:
    board = Arduino('/dev/ttyACM0')
    iterator = Iterator(board)
    iterator.start()
    print("Successfully Connected to Arduino Board")
except:
    print("ERROR: Could Not Connect to Arduino Board")
    board = None
    exit()

joystick_x = board.get_pin("a:0:i")
joystick_y = board.get_pin("a:1:i")
joystick_switch = board.digital[3]

dt = 0.1
val_x, val_y, val_s = .5, .5, 0

joystick_switch.write(1)

while True:
    time.sleep(dt)
    val_x = joystick_x.read()
    val_y = joystick_y.read()
    val_s = joystick_switch.read()
    print(val_x,',',val_y)

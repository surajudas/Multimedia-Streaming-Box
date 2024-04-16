#for complete tutorial - https://youtu.be/vRR47a6IwFM

import pyfirmata
import keyboard       #keyboard library from - https://github.com/boppreh/keyboard
import time


board = pyfirmata.Arduino('/dev/ttyACM0')   #Find the port from arduino ide

it = pyfirmata.util.Iterator(board)
it.start()


VRX = board.get_pin('a:1:i')
VRY = board.get_pin('a:2:i')
pushbutton = board.get_pin('d:8:i') #pyfirmata do not have the input pullup may be solder it joystick
x=0.5
y=0.5
sw = 0
while True:
    if VRX.read() == None:
        pass
    else:
        print("VRX: ",VRX.read() , end="  ")
    time.sleep(0.1)
    y = VRY.read()
    print("VRY: ",y, end ="     ")
    time.sleep(0.1)
    print("sw_state: ",sw)
    time.sleep(0.1)
    
    vrx_down_s = VRX.read()
    if vrx_down_s > 0.9:
        keyboard.press("s")
    elif vrx_down_s>0.3 and vrx_down_s<0.6:
        keyboard.release("s")
        
    vrx_up_w = VRX.read()
    if vrx_up_w <0.09:
        keyboard.press("w")
    elif vrx_up_w >0.09 and vrx_up_w<1.0:
        keyboard.release("w")
        
    vry_left_a =VRY.read()
    if vry_left_a <0.09:
        keyboard.press("d")
    elif vry_left_a >0.09 and vry_left_a<1.0:
        keyboard.release("d")
        
    vry_right_d = VRY.read()
    if vry_right_d > 0.9:
        keyboard.press("a")
    elif vry_right_d >0.3 and vry_right_d<0.6:
        keyboard.release("a")
        
    sw = pushbutton.read()
    if sw == 0:
        keyboard.press("space")#pullup resistor connected to joystick 
    elif sw ==1:
        keyboard.release("space")
        
        
        
        
    #vrx up=1.0
    #vrx down>0.08
    #vry left > 0.08
    #vry rigth =01.0

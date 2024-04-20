import time
import RPi.GPIO as GPIO
import os
import subprocess

GPIO.setmode(GPIO.BCM)

pin_to_ldr = 23

GPIO.setup(pin_to_ldr, GPIO.IN)

last_state = None

while True:
    if GPIO.input(pin_to_ldr):
        if last_state != 1:
            # Get the current state of the display
            display_state = subprocess.check_output(['vcgencmd', 'display_power']).decode('utf-8')[-2]
            # Toggle the display state
            new_state = '0' if display_state == '1' else '1'
            os.system(f'vcgencmd display_power {new_state}')
            last_state = 1
    else:
        print("Light detected")
        last_state = 0  

    time.sleep(0.1)
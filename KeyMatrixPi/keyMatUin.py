import RPi.GPIO as GPIO
from evdev import UInput, ecodes as e

# Define keypad matrix layout
KEYS = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

# Define GPIO pins for rows and columns
ROW_PINS = [17, 18, 27, 22]
COL_PINS = [23, 24, 25, 5]  # Adjust pin numbers according to your setup

def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in ROW_PINS + COL_PINS:
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def read_keypad():
    for col_num, col_pin in enumerate(COL_PINS):
        GPIO.output(col_pin, GPIO.LOW)
        for row_num, row_pin in enumerate(ROW_PINS):
            if GPIO.input(row_pin) == GPIO.LOW:
                return KEYS[row_num][col_num]
        GPIO.output(col_pin, GPIO.HIGH)
    return None

def main():
    setup()
    ui = UInput()

    try:
        while True:
            key = read_keypad()
            if key:
                if key.isdigit():
                    ui.write(e.EV_KEY, e.KEY_1 + int(key))
                elif key == 'A':
                    ui.write(e.EV_KEY, e.KEY_LEFT)
                elif key == 'B':
                    ui.write(e.EV_KEY, e.KEY_DOWN)
                elif key == 'C':
                    ui.write(e.EV_KEY, e.KEY_UP)
                elif key == 'D':
                    ui.write(e.EV_KEY, e.KEY_RIGHT)
                ui.syn()
    finally:
        ui.close()
        GPIO.cleanup()

if __name__ == "__main__":
    main()

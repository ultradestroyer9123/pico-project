import time
from machine import Pin
LED_PIN = Pin(0, Pin.OUT)

morse_code_msg = ".... . .-.. .-.. --- / .-- --- .-. .-.. -.. -.-.--".replace(" / ", "  ") # Hello world!

for char in morse_code_msg:
    print(char)
    if char == '.':
        LED_PIN.value(1)
        time.sleep(0.05)
        LED_PIN.value(0)
        time.sleep(0.05)
    elif char == '-':
        LED_PIN.value(1)
        time.sleep(0.15)
        LED_PIN.value(0)
        time.sleep(0.15)
    elif char == " ":
        time.sleep(0.3)
    
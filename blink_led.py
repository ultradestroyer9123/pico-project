import time
from machine import Pin
LED_PIN = Pin(0, Pin.OUT)

while(True):
    LED_PIN.value(1)
    time.sleep(1)
    LED_PIN.value(0)
    time.sleep(1)

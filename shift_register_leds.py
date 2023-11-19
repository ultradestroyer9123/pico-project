from machine import Pin
from time import sleep

# Number of shift registers
SHIFT_REGISTERS = 2

# Pin numbers for the shift register (GPIO Numbers)
DS_PIN = Pin(13, Pin.OUT) # Data pin
STCP_PIN = Pin(15, Pin.OUT) # Latch pin
SHCP_PIN = Pin(14, Pin.OUT) # Clock pin

lights = [0] * 8 * SHIFT_REGISTERS

def all_lights_on():
    for i in range(0, len(lights)):
        lights[i] = 1
    update_lights()

def all_lights_off():
    for i in range(0, len(lights)):
        lights[i] = 0
    update_lights()

def white_lights_on():
    for i in range(0, 8):
        lights[i] = 1
    update_lights()

def white_lights_off():
    for i in range(0, 8):
        lights[i] = 0
    update_lights()

def color_lights_on():
    for i in range(8, 16):
        lights[i] = 1
    update_lights()

def color_lights_off():
    for i in range(8, 16):
        lights[i] = 0
    update_lights()

def update_lights():
    #put latch down to start data sending
    SHCP_PIN.value(0)
    STCP_PIN.value(0)
    SHCP_PIN.value(1)

    #load data in reverse order
    for i in range(len(lights) - 1, -1, -1):
        SHCP_PIN.value(0)
        DS_PIN.value(lights[i])
        SHCP_PIN.value(1)

    #put latch up to store data on register
    SHCP_PIN.value(0)
    STCP_PIN.value(1)
    SHCP_PIN.value(1)

all_lights_off
sleep(1)

white_lights_on()
sleep(1)

white_lights_off()
color_lights_on()
sleep(1)

all_lights_on()
sleep(1)

all_lights_off()

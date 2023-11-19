from machine import Pin
from time import sleep
import random

# Number of shift registers
SHIFT_REGISTERS = 2

# Pin numbers for the shift register (GPIO Numbers)
DS_PIN = Pin(13, Pin.OUT) # Data pin
STCP_PIN = Pin(15, Pin.OUT) # Latch pin
SHCP_PIN = Pin(14, Pin.OUT) # Clock pin

lights = [0] * 8 * SHIFT_REGISTERS

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

def all_off():
    for led in range(len(lights)):
        lights[led] = 0

def animation_1():
    try:
        for x in range(5):
            previous = None
            for led in range(len(lights)):
                lights[led] = 1
                if previous != None:
                    lights[previous] = 0
                previous = led
                update_lights()
                sleep(0.1)
            lights[previous] = 0
            update_lights()
        sleep(0.1)
    except KeyboardInterrupt:
        all_off()
        update_lights()
        exit()
        
def randomness(oneAtATime = False):
    for x in range(20):
        try:
            if oneAtATime:
                lights[random.randint(0,len(lights)-1)] = 1
                update_lights()
                sleep(0.1)
                all_off()
                update_lights()
            else:
                for led in range(len(lights)):
                    lights[led] = random.randint(0,1)
                update_lights()
                sleep(0.1)
                all_off()
                update_lights()
        except KeyboardInterrupt:
            all_off()
            update_lights()
            exit()

print("Running animation_1.")
animation_1()
print("Running randomness type 1/2.")
randomness(True)
print("Running randomness type 2/2.")
randomness(False)

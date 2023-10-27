# Mock RPi.GPIO Library

# Constants
BCM = "BCM"
BOARD = "BOARD"
OUT = "OUT"
IN = "IN"
HIGH = 1
LOW = 0
PUD_UP = "PUD_UP"
PUD_DOWN = "PUD_DOWN"
RISING = "RISING"
FALLING = "FALLING"
BOTH = "BOTH"

# Global Variables
_pin_setup = {}
_pin_values = {}
_event_callbacks = {}

# Methods
def setwarnings(flag):
    print(f"Set warnings: {flag}")

def setmode(mode):
    print(f"Setting mode: {mode}")

def setup(pin, mode, pull_up_down=None, initial=None):
    print(f"Setting up pin {pin} with mode {mode}")
    _pin_setup[pin] = mode
    _pin_values[pin] = initial

def output(pin, value):
    if _pin_setup.get(pin) != OUT:
        raise RuntimeError("The GPIO channel has not been set up as an OUTPUT")
    print(f"Setting output for pin {pin} to {value}")
    _pin_values[pin] = value

def input(pin):
    if _pin_setup.get(pin) != IN:
        raise RuntimeError("The GPIO channel has not been set up as an INPUT")
    print(f"Reading from pin {pin}")
    return _pin_values.get(pin, LOW)

def cleanup(pin=None):
    if pin:
        print(f"Cleaning up pin {pin}")
        _pin_setup.pop(pin, None)
        _pin_values.pop(pin, None)
    else:
        print("Cleaning up all pins")
        _pin_setup.clear()
        _pin_values.clear()

def add_event_detect(pin, edge, callback=None, bouncetime=None):
    if callback:
        print(f"Adding event detect for pin {pin} on edge {edge} with callback")
        _event_callbacks[pin] = callback

def remove_event_detect(pin):
    print(f"Removing event detect for pin {pin}")
    _event_callbacks.pop(pin, None)

# PWM class for mocking PWM functions
class PWM:
    def __init__(self, pin, frequency):
        self.pin = pin
        self.frequency = frequency
        self.dc = 0
        print(f"Setting up PWM on pin {pin} with frequency {frequency}")

    def start(self, dc):
        print(f"Starting PWM on pin {self.pin} with duty cycle {dc}")
        self.dc = dc

    def ChangeDutyCycle(self, dc):
        print(f"Changing duty cycle for pin {self.pin} to {dc}")
        self.dc = dc

    def ChangeFrequency(self, frequency):
        print(f"Changing frequency for pin {self.pin} to {frequency}")
        self.frequency = frequency

    def stop(self):
        print(f"Stopping PWM on pin {self.pin}")

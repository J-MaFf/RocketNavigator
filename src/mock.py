''' 
Mock RPi.GPIO Library

GitHub Copilot: Sure, here's some documentation for the `mock.py` module:

## `mock.py` module

The `mock.py` module provides a mock implementation of the `RPi.GPIO` module for testing and development purposes. It allows you to test your code that uses the `RPi.GPIO` module without actually running it on a Raspberry Pi.

### Constants

The following constants are defined in the `mock.py` module:

- `HIGH`: A constant representing a high logic level (1).
- `LOW`: A constant representing a low logic level (0).
- `PUD_UP`: A constant representing a pull-up resistor.
- `PUD_DOWN`: A constant representing a pull-down resistor.
- `RISING`: A constant representing a rising edge.
- `FALLING`: A constant representing a falling edge.
- `BOTH`: A constant representing both rising and falling edges.

### Global Variables

The following global variables are defined in the `mock.py` module:

- `_pin_setup`: A dictionary that maps pin numbers to their setup mode (input or output).
- `_pin_values`: A dictionary that maps pin numbers to their current value (high or low).
- `_event_callbacks`: A dictionary that maps pin numbers to their event detection callbacks.

### Methods

The following methods are defined in the `mock.py` module:

- `setwarnings(flag)`: Sets the warnings flag (not implemented).
- `setmode(mode)`: Sets the GPIO mode (not implemented).
- `setup(pin, mode, pull_up_down=None, initial=None)`: Sets up a GPIO pin with the specified mode, pull-up/down resistor, and initial value.
- `output(pin, value)`: Sets the output value of a GPIO pin.
- `input(pin)`: Reads the input value of a GPIO pin.
- `cleanup(pin=None)`: Cleans up the specified GPIO pin or all pins.
- `add_event_detect(pin, edge, callback=None, bouncetime=None)`: Adds an event detection callback for a GPIO pin on the specified edge.

'''

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
    """
    Set the warning flag for the module.

    Args:
        flag (bool): The flag to set for the module.

    Returns:
        None
    """
    print(f"Set warnings: {flag}")

def setmode(mode):
    """
    Sets the mode of the rocket navigator.

    Args:
        mode (str): The mode to set the rocket navigator to.

    Returns:
        None
    """
    print(f"Setting mode: {mode}")

def setup(pin, mode, pull_up_down=None, initial=None):
    """
    Set up a pin with the specified mode and initial value (if provided).

    Args:
        pin (int): The pin number to set up.
        mode (str): The mode to set the pin to (e.g. 'IN', 'OUT', 'PWM', etc.).
        pull_up_down (str, optional): The pull-up/down resistor mode to use (e.g. 'PUD_UP', 'PUD_DOWN', etc.).
        initial (int, optional): The initial value to set the pin to (e.g. 0 or 1).

    Returns:
        None
    """
    print(f"Setting up pin {pin} with mode {mode}")
    _pin_setup[pin] = mode
    _pin_values[pin] = initial

def output(pin, value):
    """
    Sets the output value for a given GPIO pin.

    Args:
        pin (int): The GPIO pin number.
        value (int): The value to set the pin to.

    Raises:
        RuntimeError: If the GPIO channel has not been set up as an OUTPUT.
    """
    if _pin_setup.get(pin) != OUT:
        raise RuntimeError("The GPIO channel has not been set up as an OUTPUT")
    print(f"Setting output for pin {pin} to {value}")
    _pin_values[pin] = value

def input(pin):
    """
    Reads the value of the specified GPIO pin.

    Args:
        pin (int): The GPIO pin number to read.

    Returns:
        int: The value of the GPIO pin (HIGH or LOW).

    Raises:
        RuntimeError: If the GPIO channel has not been set up as an INPUT.
    """
    if _pin_setup.get(pin) != IN:
        raise RuntimeError("The GPIO channel has not been set up as an INPUT")
    print(f"Reading from pin {pin}")
    return _pin_values.get(pin, LOW)

def cleanup(pin=None):
    """
    Cleans up the specified pin or all pins if no pin is specified.

    Args:
        pin (int, optional): The pin number to clean up. Defaults to None.
    """
    if pin:
        print(f"Cleaning up pin {pin}")
        _pin_setup.pop(pin, None)
        _pin_values.pop(pin, None)
    else:
        print("Cleaning up all pins")
        _pin_setup.clear()
        _pin_values.clear()

def add_event_detect(pin, edge, callback=None, bouncetime=None):
    """
    Add an event detection for a GPIO pin.

    Args:
        pin (int): The GPIO pin number to detect events on.
        edge (str): The edge to detect events on. Must be 'rising', 'falling', or 'both'.
        callback (function, optional): A function to call when an event is detected. Defaults to None.
        bouncetime (int, optional): The time to ignore events after an initial event is detected, in milliseconds. Defaults to None.
    """
    if callback:
        print(f"Adding event detect for pin {pin} on edge {edge} with callback")
        _event_callbacks[pin] = callback

def remove_event_detect(pin):
    """
    Removes the event detection for a given pin.

    Args:
        pin (int): The pin number to remove event detection for.

    Returns:
        None
    """
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

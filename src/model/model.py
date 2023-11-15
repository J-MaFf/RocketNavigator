# Model: This will represent your rocket's data and the interaction with the Raspberry Pi's hardware.
# You'd have classes that read sensor data, interpret it, and perhaps store it. These classes wouldn't
# know how the data is displayed or what's done with it.

import RPi.GPIO as GPIO


class RocketModel:
    def __init__(self, sensors):
        self.sensors = sensors

    def readData(self):
        # Read from the sensor
        sensorValue = GPIO.input(23)
        # Return the sensor data
        return sensorValue


class SensorModel:
    """
    A class representing an abstract sensor model.

    Attributes:
    -----------
    pin : int
        The BCM pin number of the sensor.

    Methods:
    --------
    __init__(self, pin):
        Initializes the SensorModel object with the given pin number.

    readData(self):
        Reads data from the sensor and returns it.
    """

    def __init__(self, pin):
        """
        Initializes a new instance of the Model class.

        Args:
            pin (int): The BCM pin number to which the sensor is connected.
        """

        self.pin = pin

        # Set up your sensor pins and initialize them
        # For example, if you have a sensor on BCM pin 23
        GPIO.setup(pin, GPIO.IN)

    def readData(self):
        """
        Reads data from the sensor connected to the specified GPIO pin.

        Returns:
        --------
        int:
            The value read from the sensor.
        """
        # Generic method to read data from the sensor
        return GPIO.input(self.pin)


class TemperatureModel(SensorModel):
    """
    A class representing a temperature sensor model.

    Attributes:
        pin (int): The GPIO pin number to which the sensor is connected.
    """

    def __init__(self, pin):
        super().__init__(pin)

    def readData(self):
        """
        Reads data from the sensor connected to the GPIO pin and returns the converted data.

        Returns:
            float: The temperature in Fahrenheit.
        """
        sensorValue = GPIO.input(self.pin)
        return convertData(sensorValue)

    def convertData(sensorValue):
        """
        Converts the given sensor value to a temperature in Fahrenheit.

        Args:
            sensorValue (float): The sensor value to convert.

        Returns:
            float: The temperature in Fahrenheit.
        """
        return sensorValue * 1.8 + 32


class PressureModel(SensorModel):
    """
    A class representing a pressure sensor model.

    Args:
        pin (int): The GPIO pin number to which the sensor is connected.

    Attributes:
        pin (int): The GPIO pin number to which the sensor is connected.

    Methods:
        readData(): Reads data from the pressure sensor and returns it.
    """

    def __init__(self, pin):
        """
        Initializes the Model object with the specified pin.

        Args:
            pin (int): The pin number to use for the Model object.
        """
        super().__init__(pin)

    def readData(self):
        """
        Reads data from the sensor connected to the GPIO pin and returns the sensor value.

        Returns:
            int: The sensor value read from the GPIO pin.
        """
        sensorValue = GPIO.input(self.pin)
        return sensorValue


class AccelerometerModel(SensorModel):
    """
    A class representing an accelerometer sensor model.

    Args:
        pin (int): The GPIO pin number to which the sensor is connected.

    Attributes:
        pin (int): The GPIO pin number to which the sensor is connected.
    """

    def __init__(self, pin):
        """
        Initializes the Model object with the specified pin.

        Args:
            pin (int): The pin number to use for the Model object.
        """
        super().__init__(pin)

    def readData(self):
        """
        Reads data from the sensor connected to the GPIO pin and returns the sensor value.

        Returns:
            int: The sensor value read from the GPIO pin.
        """
        sensorValue = GPIO.input(self.pin)
        return sensorValue


class GyroscopeModel(SensorModel):
    """
    A class representing a gyroscope sensor model.

    Args:
        pin (int): The GPIO pin number to which the sensor is connected.

    Attributes:
        pin (int): The GPIO pin number to which the sensor is connected.
    """

    def __init__(self, pin):
        """
        Initializes the Model class with a given pin.

        Args:
            pin (int): The pin number to be used for initialization.
        """
        super().__init__(pin)

    def readData(self):
        """
        Reads the sensor data and returns the sensor value.

        Returns:
            int: The sensor value.
        """
        sensorValue = GPIO.input(self.pin)
        return sensorValue

# Model: This will represent your rocket's data and the interaction with the Raspberry Pi's hardware.
# You'd have classes that read sensor data, interpret it, and perhaps store it. These classes wouldn't
# know how the data is displayed or what's done with it.

import RPi.GPIO as GPIO
import adafruit_bmp3xx
import board
import gnss
import time
import board
import digitalio
import busio
import adafruit_lis3dh


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
        os.system("modprobe w1-gpio")
        os.system("modprobe w1-therm")

        base_dir = "/sys/bus/w1/devices/"
        device_folder = glob.glob(base_dir + "28*")[0]
        device_file = device_folder + "/w1_slave"

    def readData(self):
        """
        Reads data from the sensor connected to the GPIO pin and returns the converted data.

        Returns:
            float: The temperature in Fahrenheit.
        """
        sensorValue = GPIO.input(self.pin)
        return self.convertData()

    def read_temp_raw():
        f = open(device_file, "r")
        lines = f.readlines()
        f.close()
        return lines

    def convertData(sensorValue):
        """
        Converts the given sensor value to a temperature in Fahrenheit.

        Args:
            sensorValue (float): The sensor value to convert.

        Returns:
            float: The temperature in Fahrenheit.
        """
        lines = read_temp_raw()
        while lines[0].strip()[-3:] != "YES":
            time.sleep(0.2)
            lines = read_temp_raw()
        equals_pos = lines[1].find("t=")
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2 :]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return temp_f
        # return sensorValue * 1.8 + 32  # CHECK CONVERSION FORMULA


class Altimeter(SensorModel):
    """
    A class representing a pressure sensor model.

    Args:
        pin (int): The GPIO pin number to which   the sensor is connected.

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
        i2c = board.I2C()
        bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)

    def readData(self):
        """
        Reads data from the sensor connected to the GPIO pin and returns the sensor value.

        Returns:
            int: The sensor value read from the GPIO pin.
        """
        sensorValue = GPIO.input(self.pin)
        bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)
        temperature = bmp.temperature
        pressure = bmp.pressure
        altitude = bmp.altitude
        return temperature, pressure, altitude

    def convertData(sensorValue):
        """
        Converts the given sensor value to a pressure in Pascals.

        Args:
            sensorValue (float): The sensor value to convert.

        Returns:
            float: The pressure in Pascals.
        """
        return sensorValue * 1.8 + 32  # CHECK CONVERSION FORMULA


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
        i2c = busio.I2C(board.SCL, board.SDA)
        int1 = digitalio.DigitalInOut(board.D24)
        lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)

    def readData(self):
        """
        Reads data from the sensor connected to the GPIO pin and returns the sensor value.

        Returns:
            int: The sensor value read from the GPIO pin.
        """
        sensorValue = GPIO.input(self.pin)
        x, y, z = lis3dh.acceleration
        return x, y, z

    def convertData(sensorValue):
        """
        Converts the given sensor value to an acceleration in meters per second squared.

        Args:
            sensorValue (float): The sensor value to convert.

        Returns:
            float: The acceleration in meters per second squared.
        """
        return sensorValue * 1.8 + 32  # CHECK CONVERSION FORMULA


class GPS(SensorModel):
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
        nav = gnss.GNSS([gnss.SatelliteSystem.GPS, gnss.SatelliteSystem.GLONASS])
        super().__init__(pin)

    def readData(self):
        """
        Reads the sensor data and returns the sensor value.

        Returns:
            int: The sensor value.
        """
        sensorValue = GPIO.input(self.pin)
        nav = gnss.GNSS([gnss.SatelliteSystem.GPS, gnss.SatelliteSystem.GLONASS])
        nav.update()

        return format(nav.latitude), format(nav.longitude)

    def convertData(sensorValue):
        """
        Converts the given sensor value to a rotation in degrees per second.

        Args:
            sensorValue (float): The sensor value to convert.

        Returns:
            float: The rotation in degrees per second.
        """
        return sensorValue * 1.8 + 32  # CHECK CONVERSION FORMULA

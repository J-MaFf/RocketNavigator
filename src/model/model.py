# Model: This will represent your rocket's data and the interaction with the Raspberry Pi's hardware.
# You'd have classes that read sensor data, interpret it, and perhaps store it. These classes wouldn't
# know how the data is displayed or what's done with it.

import glob
import os
import RPi.GPIO as GPIO
import adafruit_bmp3xx
import board
import time
import board
import digitalio
import busio

# import adafruit_lis3dh
import adafruit_l3gd20
import adafruit_adxl34x


class RocketModel:
    def __init__(self):  # , sensors):
        self.sensors = []

    def initSensors(self, sensors):
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

    def __init__(self, pin, address):
        super().__init__(pin)
        os.system("modprobe w1-gpio")  # what are these
        os.system("modprobe w1-therm")  # Might not be needed

        base_dir = "/sys/bus/w1/devices/"
        # print(pin)
        device_folder = glob.glob(base_dir + str(pin) + "*")[address]
        # 28 should be pin number
        # This needs to be changed to have a device folder for all the sensors
        device_file = device_folder + "/w1_slave"
        self.sensor = device_file

    def readData(self):
        """
        Reads data from the sensor connected to the GPIO pin and returns the converted data.

        Returns:
            float: The temperature in Fahrenheit.
        """
        sensorValue = GPIO.input(
            self.pin
        )  # I dont think this is needed as one wire protocol is used

        return self.convertData(self.sensor)

    def convertData(self, device_file):
        """
        Converts the given sensor value to a temperature in Fahrenheit.

        Args:
            sensorValue (float): The sensor value to convert.

        Returns:
            float: The temperature in celcius.
        """
        # print(device_file)
        lines = self.read_temp_raw(device_file)
        while lines[0].strip()[-3:] != "YES":
            time.sleep(0.2)
            lines = self.read_temp_raw(device_file)
        equals_pos = lines[1].find("t=")
        if equals_pos != -1:
            temp_string = lines[1][equals_pos + 2 :]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return temp_c
        # return sensorValue * 1.8 + 32  # CHECK CONVERSION FORMULA

    def read_temp_raw(self, device_file):
        """
        Read the raw temperature data from the device file.

        Args:
            device_file (str): The path to the device file.

        Returns:
            list: A list of strings representing the lines read from the file.
        """
        f = open(device_file, "r")
        lines = f.readlines()
        f.close()
        return lines


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
        temperature = self.bmp.temperature
        pressure = self.bmp.pressure
        altitude = self.bmp.altitude
        return temperature, pressure, altitude


class AccelerometerModel(SensorModel):
    """
    A class representing an accelerometer sensor model.

    Args:
        pin (int): The GPIO pin number to which the sensor is connected.

    Attributes:
        pin (int): The GPIO pin number to which the sensor is connected.
    """

    def __init__(self):  # , clkPin, pin):
        """
        Initializes the Model object with the specified pin.

        Args:
            pin (int): The pin number to use for the Model object.
        """
        i2c = board.I2C()
        address = "";
        self.accelerometer = adafruit_adxl34x.ADXL343(i2c, address)
        """
        super().__init__(pin)
        self.clkPin = clkPin
        i2c = busio.I2C(board.SCL, board.SDA)
        int1 = digitalio.DigitalInOut(board.D24)
        lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)
        """

    def readData(self):
        """
        Reads data from the sensor connected to the GPIO pin and returns the sensor value.

        Returns:
            int: The sensor value read from the GPIO pin.
        """
        value = self.accelerometer.acceleration
        print(value)
        """
        sensorValue = GPIO.input(self.pin)
        x, y, z = lis3dh.acceleration
        return x, y, z
        """


class GPSModel(SensorModel):
    """
    https://gpsd.gitlab.io/gpsd/gpsd_json.html
    A class representing a GPS sensor model.

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
        gps = serial.Serial(SERIAL_PORT)

    def readData(self):
        """
        Reads the sensor data and returns the sensor value.

        Returns:
            int: The sensor value.
        """
        data = gps.readline()
        message = data[0:6]
        if message == "$GPRMC":
            parts = data.split(",")
        else:
            longitude = parts[5]
            latitude = parts[3]
            return longitude, latitude


# TODO: Finish barometer model
class BarometerModel(SensorModel):
    """
    A class representing a barometer sensor model.

    Args:
        pin (int): The GPIO pin number to which the sensor is connected.

    Attributes:
        pin (int): The GPIO pin number to which the sensor is connected.
    """

    def __init__(self, clkPin, pin):
        """
        Initializes the Model class with a given pin.

        Args:
            pin (int): The pin number to be used for initialization.
        """
        super().__init__(pin)
        self.clkPin = clkPin
        i2c = board.I2C()
        bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)

    def readData(self):
        """
        Reads the sensor data and returns the sensor value.

        Returns:
            int: The sensor value.
        """
        sensorValue = GPIO.input(self.pin)
        bmp = adafruit_bmp3xx.BMP3XX_I2C(self.i2c)
        temperature = bmp.temperature
        pressure = bmp.pressure
        altitude = bmp.altitude
        return temperature, pressure, altitude


class GyroSensor(SensorModel):
    """
    A class representing a Gyro model.

    Args:
        pin (int): The GPIO pin number to which the sensor is connected.

    Attributes:
        pin (int): The GPIO pin number to which the sensor is connected.
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
        i2c = board.I2C()
        self.sensor = adafruit_l3gd20.L3GD20_I2C(i2c)

    def readData(self):
        """
        Reads data from the sensor connected to the specified GPIO pin.

        Returns:
        --------
        int:
            The value read from the sensor.
        """
        # Generic method to read data from the sensor
        gyro_data = self.sensor.gyro
        return gyro_data

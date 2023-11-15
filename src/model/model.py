# Model: This will represent your rocket's data and the interaction with the Raspberry Pi's hardware.
# You'd have classes that read sensor data, interpret it, and perhaps store it. These classes wouldn't
# know how the data is displayed or what's done with it.

import RPi.GPIO as GPIO


class RocketModel:
    sensors = {}

    def __init__(self, sensors):
        # Set up the GPIO using the BCM (Broadcom SOC channel) numbering
        GPIO.setmode(GPIO.BCM)
        # Set up your sensor pins and initialize them
        # For example, if you have a sensor on BCM pin 23
        GPIO.setup(23, GPIO.IN)

        this.sensors = sensors

    def get_sensor_data(self):
        # Read from the sensor
        sensor_value = GPIO.input(23)
        # Return the sensor data
        return sensor_value


class SensorModel:
    def __init__(self, pin):
        self.pin = pin

        # Set up your sensor pins and initialize them
        # For example, if you have a sensor on BCM pin 23
        GPIO.setup(pin, GPIO.IN)

    def readData(self):
        # Generic method to read data from the sensor
        return GPIO.input(self.pin)


class TemperatureModel(SensorModel):
    def __init__(self, pin):
        super().__init__(pin)

    def readData(self):
        # Read from the sensor
        sensor_value = GPIO.input(self.pin)
        # Return the sensor data
        return sensor_value


class PressureModel(SensorModel):
    def __init__(self, pin):
        super().__init__(pin)

    def readData(self):
        # Read from the sensor
        sensor_value = GPIO.input(self.pin)
        # Return the sensor data
        return sensor_value


class AccelerometerModel(SensorModel):
    def __init__(self, pin):
        super().__init__(pin)

    def readData(self):
        # Read from the sensor
        sensor_value = GPIO.input(self.pin)
        # Return the sensor data
        return sensor_value


class GyroscopeModel(SensorModel):
    def __init__(self, pin):
        super().__init__(pin)

    def readData(self):
        # Read from the sensor
        sensor_value = GPIO.input(self.pin)
        # Return the sensor data
        return sensor_value

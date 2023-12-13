# This is the middleman between your Model and View. It will control the flow of data and handle user input.
import RPi.GPIO as GPIO
from datetime import datetime

from model.model import (
    AccelerometerModel,
    BarometerModel,
    SensorModel,
    TemperatureModel,
    GyroModel,
)


class RocketController:
    """
    The RocketController class is responsible for updating the view with sensor data from the model.
    """

    def __init__(self, model, view):
        """
        Initializes the Controller class with a model and view object.

        Args:
            model: An instance of the Model class.
            view: An instance of the View class.
        """
        self.model = model
        self.view = view

        """
        temp sensors are on pin 7 (gpclk0) they are adressable through 1wire protocol
        accelerometer clock is on pin 5 (gpio9) data line is on pin 3 (gpio8)
        accelerometer 2 clock is on pin 16 (gpio4) data line is on pin 15 (gpio3)
        barometer clock is on pin 13 (gpio2) data line is on pin 11 (gpio0) (bpm338 chip) Hex address 0x77
        barometer 2 clock is on pin 22 (gpio22) data line is on pin 21 (gpio21)
        """
        # sensorPinList = self.check_sensors([7, 5, 3, 16, 15, 13, 11, 22, 21])
        # Create sensor objects
        # self.sensorObjectList = self.createSensors(sensorPinList)
        self.sensorObjectList = self.createSensors()

    def createSensors(self):  # , sensorPinList):
        """
        Creates a list of SensorModel objects from a list of pins.

        Args:
            sensorPinList (list): A list of pins to which sensors are connected.

        Returns:
            list: A list of SensorModel objects.
        """
        # TODO: Create a list of SensorModel objects
        # print(sensorPinList)
        # Create Temperature Sensor objects
        TemperatureSensor1 = TemperatureModel(28, 0)  # sensorPinList[i], 0)
        TemperatureSensor2 = TemperatureModel(28, 1)  # sensorPinList[i], 1)
        TemperatureSensor3 = TemperatureModel(28, 2)  # sensorPinList[i], 2)
        TemperatureSensor4 = TemperatureModel(28, 3)  # sensorPinList[i], 3)
        # Create Accelerometer Sensor object
        AccelerometerSensor1 = (
            AccelerometerModel()
        )  # sensorPinList[i], sensorPinList[i + 1]
        # Create Barometer Sensor object
        BarometerSensor1 = BarometerModel()  # sensorPinList[i], sensorPinList[i + 1])
        # Create Gyro sensor object
        GyroSensor = GyroModel()

        # Return list of sensor objects
        sensorList = [
            TemperatureSensor1,
            TemperatureSensor2,
            TemperatureSensor3,
            TemperatureSensor4,
            AccelerometerSensor1,
            # AccelerometerSensor2,
            BarometerSensor1,
            # BarometerSensor2,
            GyroSensor,
        ]
        # print(sensorList)
        return sensorList

    def update_view(self):
        """
        Updates the view with the latest sensor data from the model.

        """
        # print(self.sensorObjectList)
        data = []
        data.append(datetime.now())
        for sensor in self.sensorObjectList:
            for point in sensor.readData():
                data.append(point)
            # line return between each sensor
        self.view.display_data(data)

    def check_sensors(self, pinList):
        """
        Checks the given pins for connected sensors. Returns a list of pins with connected sensors.

        Returns:
            list: A list of pins connected to sensors.
        """
        connected_sensors = []
        disconnected_sensors = []

        GPIO.setmode(GPIO.BCM)

        for (
            pin
        ) in (
            pinList
        ):  # TODO: Check to see if all sensors output HIGH when connected, or this won't work
            GPIO.setup(pin, GPIO.IN)
            if GPIO.input(pin):
                connected_sensors.append(pin)
            else:
                disconnected_sensors.append(pin)
        print("Connected sensors: ", connected_sensors)
        print("Disconnected sensors: ", disconnected_sensors)
        return connected_sensors

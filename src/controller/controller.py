# This is the middleman between your Model and View. It will control the flow of data and handle user input.
import RPi.GPIO as GPIO

from model.model import AccelerometerModel, SensorModel, TemperatureModel


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
        sensorPinList = self.check_sensors([7, 5, 3, 16, 15, 13, 11, 22, 21])
        # Create sensor objects
        self.createSensors(sensorPinList)

    def createSensors(self, sensorPinList):
        """
        Creates a list of SensorModel objects from a list of pins.

        Args:
            sensorPinList (list): A list of pins to which sensors are connected.

        Returns:
            list: A list of SensorModel objects.
        """
        # TODO: Create a list of SensorModel objects
        i = 0
        # Create Temperature Sensor object
        TemperatureSensor = TemperatureModel(sensorPinList[i], addresses)
        i += 1
        # Create Accelerometer Sensor object
        AccelerometerSensor1 = AccelerometerModel(
            sensorPinList[i], sensorPinList[i + 1]
        )
        i += 2
        AccelerometerSensor2 = AccelerometerModel(
            sensorPinList[i], sensorPinList[i + 1]
        )
        i += 2
        # Create Barometer Sensor object
        BarometerSensor1 = SensorModel(sensorPinList[i], sensorPinList[i + 1])
        i += 2
        BarometerSensor2 = SensorModel(sensorPinList[i], sensorPinList[i + 1])
        i += 2
        


    def update_view(self):
        """
        Updates the view with the latest sensor data from the model.
        """
        data = self.model.readData()
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

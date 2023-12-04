# This is the middleman between your Model and View. It will control the flow of data and handle user input.
import RPi.GPIO as GPIO


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

    def update_view(self):
        """
        Updates the view with the latest sensor data from the model.
        """
        data = self.model.get_sensor_data()
        self.view.display_data(data)

    def check_sensors(self, pinList):
        """
        Checks the given pins for connected sensors. Returns a list of pins with connected sensors.

        Returns:
            list: A list of pins connected to sensors.
        """
        connected_sensors = []

        GPIO.setmode(GPIO.BCM)

        for pin in pinList:
            GPIO.setup(pin, GPIO.IN)
            if GPIO.input(pin):
                connected_sensors.append(pin)

        return connected_sensors

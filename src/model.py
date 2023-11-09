# Model: This will represent your rocket's data and the interaction with the Raspberry Pi's hardware.
# You'd have classes that read sensor data, interpret it, and perhaps store it. These classes wouldn't
# know how the data is displayed or what's done with it.


class RocketModel:
    def __init__(self):
        pass  # Initialize sensors, GPIO pins, etc.

    def get_sensor_data(self):
        # Code to read from sensors
        return sensor_data

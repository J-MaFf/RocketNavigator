import mock as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set the GPIO pin where the sensor is connected
SENSOR_PIN = 17

# Set the GPIO pin to input mode
GPIO.setup(SENSOR_PIN, GPIO.IN)

try:
    while True:
        # Read sensor value
        sensor_value = GPIO.input(SENSOR_PIN)

        # Do something with the sensor value
        print(f"Sensor value: {sensor_value}")

        # Wait for a bit before reading again
        time.sleep(1)

except KeyboardInterrupt:
    print("Cleaning up...")
    GPIO.cleanup()

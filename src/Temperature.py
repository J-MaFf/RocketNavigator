import board
import analogio


def getTemp(analogin):
    millivolts = analogin.value * (analogin.reference_voltage * 1000 / 65535)
    temp_C = (millivolts - 500) / 10
    temp_F = (temp_C * 9 / 5) + 32

import board
import adafruit_bmp3xx

# https://docs.circuitpython.org/projects/bmp3xx/en/latest/api.html#adafruit_bmp3xx.BMP3XX.altitude


def getTempt():
    temperature = bmp.temperature
    pressure = bmp.pressure
    altitude = bmp.altitude
    return temperature


# float


def getPres():
    pressure = bmp.pressure
    return pressure


# float


def getAltit():
    altitude = bmp.altitude
    return altitude


# float


def reads():
    return getTempt(), getPres(), getAltit()


i2c = board.I2C()
bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)
temperature = bmp.temperature
pressure = bmp.pressure
altitude = bmp.altitude

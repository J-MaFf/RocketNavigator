import gnss

# https://content.u-blox.com/sites/default/files/products/documents/GNSS-Antennas_AppNote_%28UBX-15030289%29.pdf
# https://docs.circuitpython.org/en/8.2.x/shared-bindings/gnss/index.html#


def getLat():
    return format(nav.latitude)


def getLong():
    return format(nav.longitude)


def getUpdate():
    nav.update()


locate = gnss.GNSS([gnss.SatelliteSystem.GPS, gnss.SatelliteSystem.GLONASS])

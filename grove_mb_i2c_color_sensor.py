# Grove I2C color sensor V1.2 pour microbit
# F. SAULIN 2022

from microbit import *
import time

class GroveI2CColorSensor:

    def __init__(self):
        # initialisation du capteur
        self.set_register(0x39,0x81,0x00)
        self.set_register(0x39,0x83,0x03)
        self.set_register(0x39,0x82,0x10)
        self.set_register(0x39,0x87,0x00)
        self.set_register(0x39,0x80,0x03)

    def set_register(self, add, reg, val):
        val = bytes((reg, val))
        i2c.write(add, val)
        sleep(10)

    def get_register(self, add, reg):
        i2c.write(add, reg)
        sleep(10)
        data = i2c.read(add,1)
        sleep(10)
        return data

    def read_rgbc_raw(self):
        # Lecture des registes ADC les uns après les autres
        raw_color = []
        for i in range(8):
            register = bytes((0x90 | i,))
            value = self.get_register(0x39, register)
            try:
                val_int = int.from_bytes(value, "big")
            except:
                val_int = 0
            raw_color.append(val_int)
            sleep(10)

        return (raw_color[0],raw_color[1],raw_color[2],raw_color[3],
                raw_color[4],raw_color[5],raw_color[6],raw_color[7])

    def read_rgbc(self):
        # Lecture des registes ADC les uns après les autres
        raw_color = []
        for i in range(8):
            register = bytes((0x90 | i,))
            value = self.get_register(0x39, register)
            try:
                val_int = int.from_bytes(value, "big")
            except:
                val_int = 0
            raw_color.append(val_int)
            sleep(10)
        # calcul les valeurs
        green = raw_color[1] * 256 + raw_color[0]
        red = raw_color[3] * 256 + raw_color[2]
        blue = raw_color[5] * 256 + raw_color[4]
        clear = raw_color[7] * 256 + raw_color[6]

        return (red, green, blue, clear)


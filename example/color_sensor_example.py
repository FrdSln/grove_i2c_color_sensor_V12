from microbit import *
import  grove_mb_i2c_color_sensor

# Connecxion au capteur
color_sensor = grove_mb_i2c_color_sensor.GroveI2CColorSensor()

sleep(100)

# récupération des données brutes
color = color_sensor.read_rgbc_raw()
print(color)

# données mises en forme : rouge - vert - bleu - clair
color = color_sensor.read_rgbc()
print(color)

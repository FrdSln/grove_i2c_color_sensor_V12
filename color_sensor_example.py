from microbit import *
import  grove_mb_i2c_color_sensor

# Open connection to sensor
color_sensor = grove_mb_i2c_color_sensor.GroveI2CColorSensor()

sleep(100)

#color = color_sensor.read_rgbc()
#print("RGB: {},{},{} - Clear {}".format(color[0], color[1], color[2], color[3]))
#color = color_sensor.read_rgbc_word()
#print("RGBword: {},{},{} - Clear {}".format(color[0], color[1], color[2], color[3]))

color = color_sensor.read_rgbc_raw()
print(color)

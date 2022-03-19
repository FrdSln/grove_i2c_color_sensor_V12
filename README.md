Utilisation du capteur de couleur GROVE V1.2 avec une carte microbit : 

F. SAULIN - 2022


Initialisation du capteur avec un gain 16x : 

color_sensor = grove_mb_i2c_color_sensor.GroveI2CColorSensor()

Lecture des données brutes : 

color = color_sensor.read_rgbc_raw()

Lecture des données RVBC : 

color = color_sensor.read_rgbc()

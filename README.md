# Grove Color Sensor V1.2

![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)

Bibliothèque et exemple d'utilisation pour [Grove - Color Sensor V1.2](https://wiki.seeedstudio.com/Grove-I2C_Color_Sensor/)

## Utilisation

### Matériel nécessaire

- 1 Carte micro:bit
- 1 Shield
- 1 Grove Color Sensor V1.2
- Logiciel Mu

### Installation

**Copier** la bibliothèque mb_grove_i2c_color_sensor.py avec l'outil _fichiers_ de Mu.

**Flasher** le fichier exemple color_sensor_example.py

Le capteur doit être raccordé au port I2C. Les valeurs RGB de la couleur sont visibles avec REPL.

### Fonctions supportées

- Initialisation : color_sensor = grove_mb_i2c_color_sensor.GroveI2CColorSensor()
- Lecture des données brutes : color = color_sensor.read_rgbc_raw()
- Lecture des données RGBC : color = color_sensor.read_rgbc()

## Ressources

Ecrit en **micropython** à partir de la version C++ _arduino_

[https://github.com/Seeed-Studio/Grove_I2C_Color_Sensor](https://github.com/Seeed-Studio/Grove_I2C_Color_Sensor)

[https://github.com/DexterInd/GrovePi/blob/master/Software/Python/grove_i2c_color_sensor](https://github.com/DexterInd/GrovePi/blob/master/Software/Python/grove_i2c_color_sensor/)

## Versions

**Dernière version :** 1.0

[Liste des versions](https://github.com/FrdSln/grove_i2c_color_sensor_V12/tags)

## Auteur

* **F. SAULIN** ([FrdSln](https://github.com/FrdSln))

## Licence

Ce projet est sous licence ``GNU General Public License v3.0`` - voir le fichier [LICENSE.md](LICENSE.md) pour plus d'informations

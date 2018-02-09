import sys
import os
import numpy as np

#Pene
class GetData:
    def read():
        # Variables
        pizza = []
        minIng # Mínimo de elementos de cada tipo
        maxPorc # Número máximo de elementos por porción
        # Almacenamos el fichero en "file"
        file = open("small.in", "r")
        # Lectura de la primera línea con todos los datos
        param = file.readline()
        param = np.fromstring(param, dtype=int, sep=' ')

        matrix = ''
        for x in range(param[0]):

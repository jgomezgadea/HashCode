import random
import sys
import os
import numpy as np
import operator

class GetValues:
    def read():
        # Almacenamos el fichero en "file"
        file = open("dc.in", "r")
        # Lectura de la primera línea:
        param = file.readline()
        # Cada parámetro será un elemento del array:
        param = np.fromstring(param, dtype=int, sep=' ')

        # Habrá una lista de errores por cada fila
        for x in range(param[0]):
            errores[x] = []
        # Para cada slot no disponible...
        for x in range(param[2]):
            # Se cogen sus coordenadas y se almacenan en "errores"
            slot = file.readline()
            slot = np.fromstring(slot, dtype=int, sep=' ')
            errores[slot[0]].append(slot[1])

        for x in range(param[0]):
            errores[x] = sorted(errores[x])

        # TODO Falta que cree los diccionarios "huecos" y "servidores"

# Función main
def main(argv):
    # Variables
    global errores
    errores = {}
    global huecos
    huecos = {}
    global servidores
    servidores = {}
    # Funciones
    GetValues.read()
    print(errores)
    print(huecos)
    print(servidores)
    # TODO Crear un array en el que se guarde la posición donde irán los servidores
    # TODO Crear un array que guarde los servidores que tendrá cada pool
    # TODO Crear un archivo que contenga los resultados
    pass

if __name__ == "__main__":
    main(sys.argv)

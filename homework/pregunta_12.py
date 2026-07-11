"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contenga como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """

    resultado = {}

    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")

            letra = columnas[0]
            pares = columnas[4].split(",")

            suma = 0
            for par in pares:
                valor = int(par.split(":")[1])
                suma += valor

            if letra in resultado:
                resultado[letra] += suma
            else:
                resultado[letra] = suma

    return resultado
print(pregunta_12())

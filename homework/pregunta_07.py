"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla
    contiene un valor posible de la columna 1 y una lista con todas las letras
    asociadas a dicho valor.

    Rta/
    [(0, ['C']),
     (1, ['E', 'B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E', 'E', 'D']),
     (4, ['E', 'B']),
     (5, ['B', 'C', 'D', 'D', 'E', 'E', 'E']),
     (6, ['C', 'E', 'A', 'B']),
     (7, ['A', 'C', 'E', 'D']),
     (8, ['E', 'D', 'E', 'A', 'B']),
     (9, ['A', 'B', 'E', 'A', 'A', 'C'])]
    """

    datos = {}

    with open("files/input/data.csv", "r") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")

            letra = columnas[0]
            numero = int(columnas[1])

            if numero not in datos:
                datos[numero] = [letra]
            else:
                datos[numero].append(letra)

    resultado = []

    for numero in sorted(datos):
        resultado.append((numero, datos[numero]))

    return resultado
print(pregunta_07())

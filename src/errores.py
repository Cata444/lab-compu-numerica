import numpy as np
import matplotlib.pyplot as plt
from cargar_datos import obtener_precios

#A1 Error de representación mes a mes
def representation_error():
    datos_csv = obtener_precios()
    for dato in datos_csv:
        print(dato)

if __name__ == "__main__":
    representation_error()
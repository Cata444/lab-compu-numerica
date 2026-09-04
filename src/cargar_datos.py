import numpy as np

def obtener_precios():
    # np.genfromtxt lee el archivo. 
    # skip_header=1 salta la primera fila donde están las palabras "Mes", "2022", etc.
    matriz_datos = np.genfromtxt('data/dolar_observado_sii_2022_2025.csv', delimiter=',', skip_header=1)
    
    # La columna 0 tiene los nombres de los meses en texto, así que tomamos desde la columna 1 hasta la 4
    solo_numeros = matriz_datos[:, 1:5]
    
    # flatten() convierte la tabla en una sola fila larga. 
    # order='F' lo hace leyendo hacia abajo (columna por columna) para ordenar por año cronológicamente.
    vector_precios = solo_numeros.flatten(order='F')
    
    return vector_precios

# Pequeña prueba para ver si funciona cuando ejecutas solo este archivo
if __name__ == "__main__":
    precios = obtener_precios()
    print("Datos cargados correctamente. Cantidad de meses:", len(precios))
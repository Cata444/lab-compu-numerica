import numpy as np
import matplotlib.pyplot as plt
from cargar_datos import obtener_precios

precios_reales = obtener_precios()


# B4. Cancelación en la máquina

#aqui usamos la calculadora de python, de 32 bits para tener error
precio_diciembre23 = np.float32(874.67)
precio_diciembre22 = np.float32(875.66)

resta_32bits = precio_diciembre23 - precio_diciembre22

# Usamos la calculadora de python, de 64 bits para tener un error mucho mas ameno
precio_diciembre23_64 = np.float64(874.67)
precio_diciembre22_64 = np.float64(875.66)

resta_64bits = precio_diciembre23_64 - precio_diciembre22_64

# imprimos para verificar que son distintas estas calculadoras con sus error
print("Resta con memoria 32 bits: ", resta_32bits)
print("Resta con memoria 64 bits: ", resta_64bits)


# B2. La ida y vuelta que no vuelve

#Toma Monto en pesos chilenos, cómpralos a dólares con el precio de un mes y
# vuélvelos a pesos con el
#mismo precio

dinero_inicial = 1000000
platita_perdida = [] 

# se recorre la lista completa con un for porque son 48 elementos
for precio_actual in precios_reales:
    
    # hay que ponerlo con 32 bits porque es el q tiene mas error 
    precio_malo = np.float32(precio_actual)
    dinero_malo = np.float32(dinero_inicial)
    
    #aqui vendo
    dolares_obtenidos = dinero_malo / precio_malo
    
    # aqui vuelvo a comprar
    pesos_recuperados = dolares_obtenidos * precio_malo
    
    # aqui veremos si es que oficialmente seguimos teniendo la misma plata que al comienzo
    plata_error = pesos_recuperados - dinero_inicial
    
    # Guardamos este pequeño error en nuestra lista
    platita_perdida.append(plata_error)

#aqui en resumen lo que hice fue ir vendiendo y despues comprando de inmediato,
#como cuando uno se arrepiente pero cada vez tiene errores mas grandes


# 3. Crear grafico


plt.plot(platita_perdida)
plt.title("Plata fantasma ida y vuelta")
plt.xlabel("Meses evaluados")
plt.ylabel("Diferencia respecto al $1.000.000 original")
plt.savefig('graficos/5_ida_y_vuelta.png')
plt.close()
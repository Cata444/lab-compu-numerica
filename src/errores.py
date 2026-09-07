import numpy as np
import cargar_datos as cd
import matplotlib.pyplot as plt
import anualidad as an
import os
######################## Funciones de error y operaciones #################################################
def registrar_evaluacion_error(ej_descripcion, punto1, punto2, valor_real, valor_aprox, error_absoluto, error_relativo, error_propagado="N/A", ruta_archivo="evaluacion_errores.csv"):
    '''
        Función para Guardar los datos recopilados en un archivo csv, guardandandolos de manera progresiva mientras avanza el programa. (Se recomienda eliminar el archivo csv antes de volver a ejecutar este codigo.) 
    '''
    fila = np.array([[
        str(ej_descripcion), str(punto1), str(punto2), str(valor_real), str(valor_aprox), str(error_absoluto), str(error_relativo),str(error_propagado)]], dtype=str)
    
    archivo_existe = os.path.isfile(ruta_archivo)
    
    with open(ruta_archivo, mode='a', encoding='utf-8') as archivo:
        if not archivo_existe:
            # Si el archivo es nuevo, escribimos los encabezados que pide el laboratorio
            archivo.write("Ejercicio_descripcion,Punto1,Punto2,Valor_Real,Valor_Aproximado,Error_Absoluto,Error_relatico,Error_Propagado\n")
        
        np.savetxt(archivo, fila, delimiter=',', fmt='%s')

def numero_cientifico(x, c_s = None, truncar = False, truncar_cifras = 2):
    '''
        Convierte un número a su representación en notación científica.
        Tambien puede truncar el número a un número de cifras significativas especificado.
    '''
    x_str = str(x)
    exp: int
    base: int
    num_flt: float
    num_flt1: np.float64
    if (c_s == None):
        exp = 0
        for i in range(len(x_str)):
            if x_str[i].isdigit():
                exp += 1
            else:
                break
        
        base = 10
        num_flt = float(x) / base ** exp
    else:
        exp = c_s
        base = 10
        num_flt = float(x) / base ** exp

    if truncar:
        num_flt1 = np.trunc(num_flt * 10 ** truncar_cifras) / 10 ** truncar_cifras
        return [np.array([np.float64(num_flt1)]), np.int64(base), np.int64(exp), np.float64(x)]
    else:  
        return [np.array([np.float64(num_flt)]), np.int64(base), np.int64(exp), np.float64(x)]

def error_absoluto(valor_real, valor_aproximado):
    '''Calcula el error absoluto entre un valor real y un valor aproximado.'''
    return np.abs(valor_real - valor_aproximado)

def error_relativo(valor_real, valor_aproximado):
    '''Calcula el error relativo entre un valor real y un valor aproximado. Te entrega un resultado en porcentaje.'''
    if valor_real == 0:
        raise ValueError("El valor real no puede ser cero para calcular el error relativo.")
    return (np.abs(valor_real - valor_aproximado) / valor_real) * 100

def comprar_dolares(monto_pesos, precio_compra):
    '''Calcula la cantidad de dólares que se pueden comprar con un monto en pesos y un precio de compra.'''
    return monto_pesos / precio_compra

def vender_dolares(cantidad_dolares, precio_venta):
    '''Calcula la cantidad de pesos que se obtienen al vender una cantidad de dólares a un precio de venta.'''
    return cantidad_dolares * precio_venta

def ganancia(monto_inicial, monto_final):
    '''Calcula la ganancia obtenida al comparar un monto inicial con un monto final.'''
    return monto_final - monto_inicial

def rentabilidad(monto_inicial, monto_final):
    '''Calcula la rentabilidad obtenida al comparar un monto inicial con un monto final. Entrega un porcentaje.'''
    if monto_inicial == 0:
        raise ValueError("El monto inicial no puede ser cero para calcular la rentabilidad.")
    return (monto_final / monto_inicial) * 100

def variacion_entre_meses(precio_mes_anterior, precio_mes_actual):
    '''Calcula la variación entre el precio de un mes anterior y el precio de un mes actual.'''
    return precio_mes_actual - precio_mes_anterior

def propagacion_resta(valor_aprox1, valor_aprox2, error_absoluto1, error_absoluto2):
    '''Calcula la propagación del error absoluto al restar dos valores aproximados.'''
    resultado = np.abs(valor_aprox2 - valor_aprox1)
    error_propagado = error_absoluto1 + error_absoluto2
    error_relativo_total = np.abs(error_propagado / resultado) if resultado != 0 else np.inf
    return [resultado, error_propagado, error_relativo_total]

def sacar_numero_redondeado_error_absoluto_relativo(datos_csv):
    '''Calcula el numero redondeado, el error absoluto y el error relativo de cada mes a partir de los datos del csv, luego devuelve una lista con tres listas para cada valor.'''
    # Usaremos tres listas para guardar los errores absolutos, relativos y truncados de cada mes
    precios_reales = []
    errores_relativos = []
    errores_absolutos = []
    numeros_redondeados = []
    # Usaremos un ciclo for para recorrer cada mes y calcular los errores de representacion
    for i in range(datos_csv.shape[0]):
        precio_observado = datos_csv[i][3]
        precios_reales.append(precio_observado)
        #Calculamos el numero redondeado que queremos,
        # y luego lo añadimos a la lista de numeros redondeados.
        numero_redondeado = np.round(precio_observado/10)*10
        numeros_redondeados.append(numero_redondeado)

        # Calculamos el error absoluto y relativo entre el precio observado y el numero redondeado, y los añadimos a sus respectivas listas.
        er_absoluto = error_absoluto(precio_observado, numero_redondeado)
        errores_absolutos.append(numero_cientifico(er_absoluto, 0, True, 2)[0])
        er_relativo = error_relativo(precio_observado, numero_redondeado)
        errores_relativos.append(numero_cientifico(er_relativo, 0, True, 2)[0])
    return [errores_absolutos, errores_relativos, numeros_redondeados, precios_reales]

#######################################################################################################

#Grafico serie mensual del dolar
def grafico_serie_mensual_dolar(precios_reales):
    """
    Genera el gráfico de línea para la serie mensual del dólar 2022-2025.
    """
    valores_y = np.array(precios_reales, dtype=float).flatten()
    
    meses_x = np.arange(len(valores_y))

    fig, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(meses_x, valores_y, marker='o', linestyle='-', color='royalblue', linewidth=2, markersize=4)
    
    ax.set_xlabel('Índice del Mes (0 = Ene 2022, 47 = Dic 2025)')
    ax.set_ylabel('Precio Dólar Observado (Pesos Chilenos)')
    ax.set_title('Serie Mensual del Dólar Observado SII (2022 - 2025)')
    
    ax.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()

#A1 Error de representación mes a mes V
def representation_error():
    # Cargamos los datos del CSV usando la funcion para obtener estos datos
    datos_csv = cd.obtener_datos()
    
    num_red_err_abs_rel = sacar_numero_redondeado_error_absoluto_relativo(datos_csv)

    # Buscamos el error relativo máximo y su índice para poder imprimir el mes y año correspondiente.
    max_er_relativo = max(num_red_err_abs_rel[1])
    ind_max_er_relativo = num_red_err_abs_rel[1].index(max_er_relativo)
    print("El error relativo máximo se encuentra en el mes", datos_csv[ind_max_er_relativo][1],"del año", datos_csv[ind_max_er_relativo][0], "con un valor de: ", numero_cientifico(max_er_relativo[0], 0, True, 2)[0][0], "%")
    for datos in range(len(num_red_err_abs_rel[3])):
        registrar_evaluacion_error(
                ej_descripcion= "A1 representacion de error en los datos",
                punto1= f"{datos_csv[datos][0]} - {datos_csv[datos][1]}",
                punto2= f"N/A",
                valor_real= f"{num_red_err_abs_rel[3][datos]}",
                valor_aprox= f"{num_red_err_abs_rel[2][datos]}",
                error_absoluto= f"{num_red_err_abs_rel[0][datos]}",
                error_relativo= f"{num_red_err_abs_rel[1][datos]}",
                ruta_archivo= "./data/evaluacion_errores.csv"
            )

    # Zona de Grafico de Barras
    meses_x = range(len(num_red_err_abs_rel[1]))
    valores_y = np.array(num_red_err_abs_rel[1], dtype=float).flatten()
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(meses_x, valores_y, color='skyblue', edgecolor='black')

    ax.set_xlabel('Índice del Mes (Enero 2022 -> Diciembre 2025)')
    ax.set_ylabel('Error Relativo (%)')
    ax.set_title('Error de representación por mes al usar 2 cifras significativas')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()

#A2 Evaluación entre dos puntos (una compra-venta) V
def evaluacion_compra_venta(monto_inicial, indice_compra, indice_venta, propio=0):
    # Cargamos los datos del CSV usando la funcion para obtener estos datos
    datos_csv = cd.obtener_datos()

    #Obtenemos los datos redondeados, con error absoluto, relativo y el numero original
    num_red_err_abs_rel = sacar_numero_redondeado_error_absoluto_relativo(datos_csv)
    if propio != 0:
        precio_aprox_compra = num_red_err_abs_rel[3][indice_compra]
        precio_aprox_venta = num_red_err_abs_rel[3][indice_venta]
        
        error_relativo_compra = num_red_err_abs_rel[1][indice_compra]
        error_relativo_venta = num_red_err_abs_rel[1][indice_venta]
        
        #Propagación
        error_relativo_total = error_relativo_compra + error_relativo_venta
    
        #Operaciones financieras
        cantidad_dolares = comprar_dolares(monto_inicial, precio_aprox_compra)
        monto_final = vender_dolares(cantidad_dolares, precio_aprox_venta)
        ganancia_obtenida = ganancia(monto_inicial, monto_final)
        rentabilidad_obtenida = rentabilidad(monto_inicial, monto_final)
    
        #Pasar a error absoluto para arrastrar a la ganancia
        error_absoluto_final = (error_relativo_total * monto_final) / 100
        
        #Calculo del error porcentual de la ganancia se ocupa valor absoluto de la ganancia para que no de negativo, y se multiplica por 100 para pasarlo a porcentaje
        if ganancia_obtenida != 0:
            error_porcentual_ganancia = (error_absoluto_final / np.abs(ganancia_obtenida)) * 100
            #print(f"Ganancia obtenida: {numero_cientifico(ganancia_obtenida, 0, True, 2)[0][0]} ± {numero_cientifico(error_absoluto_final[0], 0, True, 2)[0][0]} pesos")
            #print(f"Error porcentual de la ganancia: {numero_cientifico(error_porcentual_ganancia[0], 0, True, 2)[0][0]}%")
        else:
            error_porcentual_ganancia = float('inf') # Si la ganancia es 0, el error es infinito
            #print(f"Ganancia obtenida: {numero_cientifico(ganancia_obtenida, 0, True, 2)[0][0]} ± {numero_cientifico(error_absoluto_final[0], 0, True, 2)[0][0]} pesos")
            #print(f"Error porcentual de la ganancia: {error_porcentual_ganancia}%")
        
        return [monto_final, ganancia_obtenida, rentabilidad_obtenida, error_absoluto_final, error_porcentual_ganancia]
        
    #Tomaremos el precio redondeado y el error relativo del año y mes que nos proporcione los indices de compra y venta respectivamente
    precio_aprox_compra = num_red_err_abs_rel[2][indice_compra]
    precio_aprox_venta = num_red_err_abs_rel[2][indice_venta]
    
    error_relativo_compra = num_red_err_abs_rel[1][indice_compra]
    error_relativo_venta = num_red_err_abs_rel[1][indice_venta]
    
    #Propagación
    error_relativo_total = error_relativo_compra + error_relativo_venta

    #Operaciones financieras
    cantidad_dolares = comprar_dolares(monto_inicial, precio_aprox_compra)
    monto_final = vender_dolares(cantidad_dolares, precio_aprox_venta)
    ganancia_obtenida = ganancia(monto_inicial, monto_final)
    rentabilidad_obtenida = rentabilidad(monto_inicial, monto_final)

    #Pasar a error absoluto para arrastrar a la ganancia
    error_absoluto_final = (error_relativo_total * monto_final) / 100
    error_porcentual_ganancia = 0
    #Calculo del error porcentual de la ganancia se ocupa valor absoluto de la ganancia para que no de negativo, y se multiplica por 100 para pasarlo a porcentaje
    if ganancia_obtenida != 0:
        error_porcentual_ganancia = (error_absoluto_final / np.abs(ganancia_obtenida)) * 100
        print(f"Ganancia obtenida: {numero_cientifico(ganancia_obtenida, 0, True, 2)[0][0]} ± {numero_cientifico(error_absoluto_final[0], 0, True, 2)[0][0]} pesos")
        print(f"Error porcentual de la ganancia: {numero_cientifico(error_porcentual_ganancia[0], 0, True, 2)[0][0]}%")
    else:
        error_porcentual_ganancia = float('inf') # Si la ganancia es 0, el error es infinito
        print(f"Ganancia obtenida: {numero_cientifico(ganancia_obtenida, 0, True, 2)[0][0]} ± {numero_cientifico(error_absoluto_final[0], 0, True, 2)[0][0]} pesos")
        print(f"Error porcentual de la ganancia: {error_porcentual_ganancia}%")

    registrar_evaluacion_error(
                    ej_descripcion= "A2 Evaluacion compra-venta",
                    punto1= f"{datos_csv[indice_compra][1]}-{datos_csv[indice_compra][0]}:{num_red_err_abs_rel[2][indice_compra]}",
                    punto2= f"{datos_csv[indice_venta][1]}-{datos_csv[indice_venta][0]}:{num_red_err_abs_rel[2][indice_venta]}",
                    valor_real= f"{ganancia_obtenida}",
                    valor_aprox= f"N/A",
                    error_absoluto= f"{error_absoluto_final[0]}",
                    error_relativo= f"{error_porcentual_ganancia}",
                    ruta_archivo= "./data/evaluacion_errores.csv"
                )
    
    return [monto_final, ganancia_obtenida, rentabilidad_obtenida, error_absoluto_final, error_porcentual_ganancia]

#A5 Mejor compra y mejor venta V
def mejor_compra_venta(monto_inicial = 1000000):
    # Cargamos los datos del CSV usando la funcion para obtener estos datos como np.arrays de tamaño 4
    datos_csv = cd.obtener_datos()

    # Sacamos los numeros redondeados y errores absolutos de cada mes, con dos cifras significativas 
    num_red_real_err_abs_rel = sacar_numero_redondeado_error_absoluto_relativo(datos_csv)
    nums_reales = num_red_real_err_abs_rel[3]

    # Sacamos el mejor precio de compra y el mejor precio de venta, junto con sus indices para poder imprimir el mes y año correspondiente.
    mejor_compra = min(nums_reales)
    mejor_venta = max(nums_reales)
    ind_mejor_compra = np.where (np.array(nums_reales) == mejor_compra)[0][0]
    ind_mejor_venta = np.where (np.array(nums_reales) == mejor_venta)[0][0]
    print("El mejor precio de compra se encuentra en el mes", datos_csv[ind_mejor_compra][1],"del año", datos_csv[ind_mejor_compra][0], "con un valor de: ", mejor_compra)
    print("El mejor precio de venta se encuentra en el mes", datos_csv[ind_mejor_venta][1],"del año", datos_csv[ind_mejor_venta][0], "con un valor de: ", mejor_venta)

    # Calculamos el resultado de comprar 1,000,000 de pesos chilenos en el mejor mes de compra y venderlos en el mejor mes de venta, junto con su error relativo total.
    resultado = evaluacion_compra_venta(monto_inicial, ind_mejor_compra, ind_mejor_venta, propio=1)

    #Para el apartado grafico realizaremos un escaneo de la rentabilidad en cada mes y lo llevaremos a un grafico de barras con su error para ver como se ven los errores
    rentables = []
    errores_rentabilidad = []
    for venta in range(ind_mejor_compra, len(nums_reales)-1):
        evaluado = evaluacion_compra_venta(monto_inicial, ind_mejor_compra, venta+1, propio=1)
        
        rentabilidad_mes = evaluado[2]
        error_absoluto_pesos = evaluado[3]
        
        error_en_porcentaje = (error_absoluto_pesos / monto_inicial) * 100
        
        rentables.append(rentabilidad_mes)
        errores_rentabilidad.append(error_en_porcentaje)

    #Zona del Grafico
    meses_x = range(len(rentables))
    valores_y = np.array(rentables, dtype=float).flatten()
    errores_y = np.array(errores_rentabilidad, dtype=float).flatten()
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(meses_x, valores_y, yerr=errores_y, capsize=5, color='lightgreen', edgecolor='black', alpha=0.8)

    ax.set_xlabel('Meses de venta (posteriores al mes de compra más barato)')
    ax.set_ylabel('Rentabilidad (%)')
    ax.set_title('Rentabilidad simulada desde el mes mínimo de compra')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()

    return resultado

if __name__ == "__main__":
#Zona de uso de las funciones, solo desmarcar la que se requiera usar.
    representation_error()
    evaluacion_compra_venta(1000000, 13, 36)
    an.cancelacion()
    an.variacion_anual()
    mejor_compra_venta()

###########Usar grafico serie mensual#################
    #datos_csv = cd.obtener_datos()
    #num_red_real_err_abs_rel = sacar_numero_redondeado_error_absoluto_relativo(datos_csv)
    #precios = num_red_real_err_abs_rel[3]
    #grafico_serie_mensual_dolar(precios)